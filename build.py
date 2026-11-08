#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — grava no index.html o que antes so existia depois do JavaScript rodar.

POR QUE ISSO EXISTE
  A galeria e as duvidas eram montadas por js/main.js a partir de js/dados.js.
  Quem le a pagina sem executar JavaScript — Google Imagens e os rastreadores de
  ChatGPT e Gemini, entre outros — nao via foto nenhuma e nao via o FAQ.

O QUE FAZ
  Le js/dados.js (que continua sendo o unico arquivo que voce edita), gera o HTML
  da galeria e das duvidas, o JSON-LD do FAQ, e grava tudo dentro do index.html
  entre marcadores. Regenera tambem o sitemap.xml com as imagens.

COMO USAR
  python3 build.py           depois de qualquer mudanca em js/dados.js

  Se voce esquecer de rodar, nada quebra: o main.js percebe que o HTML esta
  diferente do dados.js e volta a montar a galeria sozinho, como antes.
"""
import io, os, re, json, datetime

RAIZ = os.path.dirname(os.path.abspath(__file__))
def caminho(*p): return os.path.join(RAIZ, *p)

# ---------------------------------------------------------------- dimensoes
def tamanho_webp(arq):
    """Largura e altura de um .webp, sem depender de biblioteca externa."""
    with open(arq, 'rb') as f:
        d = f.read(32)
    if d[:4] != b'RIFF' or d[8:12] != b'WEBP':
        raise ValueError('nao e webp: %s' % arq)
    fmt = d[12:16]
    if fmt == b'VP8 ':
        return (int.from_bytes(d[26:28], 'little') & 0x3FFF,
                int.from_bytes(d[28:30], 'little') & 0x3FFF)
    if fmt == b'VP8L':
        n = int.from_bytes(d[21:25], 'little')
        return ((n & 0x3FFF) + 1, ((n >> 14) & 0x3FFF) + 1)
    if fmt == b'VP8X':
        return (int.from_bytes(d[24:27], 'little') + 1,
                int.from_bytes(d[27:30], 'little') + 1)
    raise ValueError('formato webp desconhecido: %s' % fmt)

# ---------------------------------------------------------------- leitura
def ler_dados():
    s = io.open(caminho('js', 'dados.js'), encoding='utf-8').read()

    bloco = re.search(r'trabalhos:\s*\[(.*?)\n  \]', s, re.S)
    if not bloco: raise SystemExit('ERRO: array "trabalhos" nao encontrado em dados.js')
    trabalhos = []
    for linha in re.finditer(r'\{\s*img:"([^"]+)"\s*,\s*cap:"([^"]+)"\s*,\s*alt:"([^"]+)"\s*\}', bloco.group(1)):
        trabalhos.append({'img': linha.group(1), 'cap': linha.group(2), 'alt': linha.group(3)})

    bloco = re.search(r'duvidas:\s*\[(.*?)\n  \]', s, re.S)
    if not bloco: raise SystemExit('ERRO: array "duvidas" nao encontrado em dados.js')
    duvidas = []
    for linha in re.finditer(r'\{\s*p:"([^"]+)"\s*,\s*\n?\s*r:"((?:[^"\\]|\\.)*)"\s*\}', bloco.group(1), re.S):
        duvidas.append({'p': linha.group(1), 'r': linha.group(2)})

    if not trabalhos: raise SystemExit('ERRO: nenhum trabalho lido')
    if not duvidas:   raise SystemExit('ERRO: nenhuma duvida lida')
    return trabalhos, duvidas

def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;')
             .replace('>', '&gt;').replace('"', '&quot;'))

# ---------------------------------------------------------------- geracao
def html_galeria(trabalhos):
    out = []
    for i, o in enumerate(trabalhos):
        arq = caminho('img', o['img'] + '.webp')
        if not os.path.exists(arq):
            raise SystemExit('ERRO: falta a imagem %s (citada em dados.js)' % arq)
        w, h = tamanho_webp(arq)
        legenda = o['cap'].split('·')[-1].strip()
        out.append(
            '<button class="work reveal" data-cap="%s">'
            '<img src="img/%s.webp" alt="%s" width="%d" height="%d"%s decoding="async">'
            '<span class="cap">%s</span></button>'
            % (esc(o['cap']), esc(o['img']), esc(o['alt']), w, h,
               ' loading="lazy"' if i else '', esc(legenda)))
    return '\n        '.join(out)

def html_duvidas(duvidas):
    return '\n        '.join(
        '<details class="acc__item reveal"><summary><span>%s</span>'
        '<i aria-hidden="true"></i></summary><div class="acc__corpo"><p>%s</p></div></details>'
        % (esc(d['p']), d['r']) for d in duvidas)

def jsonld_faq(duvidas):
    return json.dumps({
        '@context': 'https://schema.org', '@type': 'FAQPage',
        'mainEntity': [{'@type': 'Question', 'name': d['p'],
                        'acceptedAnswer': {'@type': 'Answer',
                                           'text': re.sub(r'<[^>]+>', '', d['r'])}}
                       for d in duvidas]}, ensure_ascii=False, indent=1)

# ---------------------------------------------------------------- escrita
def trocar(s, marca, conteudo):
    ini, fim = '<!--%s:inicio-->' % marca, '<!--%s:fim-->' % marca
    padrao = re.compile(re.escape(ini) + '.*?' + re.escape(fim), re.S)
    if not padrao.search(s):
        raise SystemExit('ERRO: marcadores de "%s" nao encontrados no index.html' % marca)
    return padrao.sub(lambda _: '%s\n        %s\n        %s' % (ini, conteudo, fim), s)

def sitemap(trabalhos):
    hoje = datetime.date.today().isoformat()
    imgs = '\n'.join(
        '    <image:image><image:loc>https://andretattoo.com.br/img/%s.webp</image:loc>'
        '<image:title>%s</image:title><image:caption>%s</image:caption></image:image>'
        % (esc(o['img']), esc(o['cap'].replace('·', '-')), esc(o['alt'])) for o in trabalhos)
    outras = ''
    import paginas as _p
    for pg in _p.PAGINAS:
        outras += ('  <url>\n    <loc>https://andretattoo.com.br/%s</loc>\n'
                   '    <lastmod>%s</lastmod>\n    <changefreq>monthly</changefreq>\n'
                   '    <priority>0.9</priority>\n  </url>\n' % (pg['slug'], hoje))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
            '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
            '  <url>\n    <loc>https://andretattoo.com.br/</loc>\n'
            '    <lastmod>%s</lastmod>\n    <changefreq>monthly</changefreq>\n'
            '    <priority>1.0</priority>\n%s\n  </url>\n'
            '%s'
            '  <url>\n    <loc>https://andretattoo.com.br/clube-15</loc>\n'
            '    <lastmod>%s</lastmod>\n    <changefreq>monthly</changefreq>\n'
            '    <priority>0.8</priority>\n  </url>\n</urlset>\n' % (hoje, imgs, outras, hoje))


# ---------------------------------------------------------------- paginas de estilo
def pedaco(html, ini, fim):
    a = html.index(ini); b = html.index(fim, a) + len(fim)
    return html[a:b]

def pagina_html(pg, alts, nav, rodape, estudio_ld):
    import paginas as _p
    BASE = 'https://andretattoo.com.br/'
    url = BASE + pg['slug']

    blocos = []
    for _i, (titulo, paras) in enumerate(pg['blocos']):
        blocos.append(('  <section class="conteudo%s"><div class="wrap">\n'
                       % (' bloco' if _i % 2 else '')) +
                      '    <h2 class="reveal">%s</h2>\n%s\n  </div></section>'
                      % (esc(titulo),
                         '\n'.join('    <p class="reveal">%s</p>' % esc(t) for t in paras)))
    fotos = []
    for i, nome in enumerate(pg['galeria']):
        arq = caminho('img', nome + '.webp')
        if not os.path.exists(arq):
            raise SystemExit('ERRO: %s citada em paginas.py nao existe' % arq)
        w, h = tamanho_webp(arq)
        fotos.append('<button class="work reveal" data-cap="%s">'
                     '<img src="img/%s.webp" alt="%s" width="%d" height="%d" '
                     'loading="lazy" decoding="async"></button>'
                     % (esc(alts[nome]['cap']), esc(nome), esc(alts[nome]['alt']), w, h))

    duvidas = '\n        '.join(
        '<details class="acc__item reveal"><summary><span>%s</span>'
        '<i aria-hidden="true"></i></summary><div class="acc__corpo"><p>%s</p></div></details>'
        % (esc(q), esc(a)) for q, a in pg['faq'])

    irmas = '\n        '.join(
        '<a class="btn ghost" href="%s">%s</a>' % (s_, esc(_p.TITULOS_CURTOS[s_]))
        for s_ in pg['irmas'])

    ld = {'@context': 'https://schema.org', '@graph': [
      {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Início', 'item': BASE},
        {'@type': 'ListItem', 'position': 2, 'name': _p.TITULOS_CURTOS[pg['slug']], 'item': url}]},
      {'@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q,
         'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in pg['faq']]},
      {'@type': 'Service', 'name': pg['servico'], 'serviceType': pg['servico'],
       'url': url, 'description': pg['desc'],
       'provider': {'@id': BASE + '#estudio'},
       'areaServed': [{'@type': 'City', 'name': 'São Paulo'},
                      {'@type': 'Place', 'name': 'Zona Leste de São Paulo'}]},
      estudio_ld,
    ]}

    gal_titulo = pg.get('galeria_titulo', 'Trabalhos')
    gal_nota = ('    <p class="frase reveal">%s</p>\n' % esc(pg['galeria_nota'])) if pg.get('galeria_nota') else ''

    return """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="theme-color" content="#F3F1EC">
<link rel="canonical" href="%(url)s">

<meta property="og:type" content="website">
<meta property="og:site_name" content="André Tattoo">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(url)s">
<meta property="og:image" content="https://andretattoo.com.br/img/og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="pt_BR">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" href="img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400;1,6..96,500&family=Archivo:wght@400;500;600&family=DM+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="css/style.css">

<script type="application/ld+json">
%(ld)s
</script>
<script>document.documentElement.className += ' js';</script>
</head>
<body>

%(nav)s

<main id="topo">
  <section class="hero hero--texto">
    <div class="wrap">
      <div>
        <nav class="migalhas" aria-label="Você está em">
          <a href="/">Início</a> <span aria-hidden="true">·</span> <span>%(curto)s</span>
        </nav>
        <span class="eyebrow"><b>●</b>&nbsp; %(eyebrow)s</span>
        <h1>%(h1)s</h1>
        <p class="lead">%(lead)s</p>
        <div class="ctas">
          <a class="btn" href="https://wa.me/5511982713543" target="_blank" rel="noopener" data-wa="topo"><span class="dot"></span>Falar comigo no WhatsApp</a>
          <a class="btn ghost" href="#trabalhos">Ver trabalhos</a>
        </div>
      </div>
    </div>
  </section>

%(blocos)s

  <section id="trabalhos">
    <div class="wrap">
      <div class="head reveal"><div><span class="eyebrow">%(gal_titulo)s</span></div></div>
%(gal_nota)s      <div class="gallery" id="gallery" data-fonte="pagina">
        %(fotos)s
      </div>
      <div class="gallery-foot">
        <span>Tem muito mais no Instagram.</span>
        <a class="btn ghost sm" href="https://www.instagram.com/andretatuadoor/" target="_blank" rel="noopener">@andretatuadoor</a>
      </div>
    </div>
  </section>

  <section class="faq" id="duvidas">
    <div class="wrap">
      <div class="head reveal"><div><span class="eyebrow">Dúvidas</span>
        <h2 style="margin-top:14px">Antes de <em>perguntar</em>.</h2></div></div>
      <div class="acc" id="acc" data-fonte="pagina">
        %(duvidas)s
      </div>
    </div>
  </section>

  <section class="bloco">
    <div class="wrap">
      <h2 class="reveal">Veja também</h2>
      <div class="ctas reveal">
        %(irmas)s
      </div>
    </div>
  </section>

  <section class="final" id="fim">
    <div class="wrap reveal">
      <span class="eyebrow">Sua vez</span>
      <h2>Bora tirar essa ideia <em>do papel?</em></h2>
      <p>Me manda uma mensagem contando o que você imagina. Eu respondo pessoalmente.</p>
      <a class="btn" href="https://wa.me/5511982713543" target="_blank" rel="noopener" data-wa="obras"><span class="dot"></span>Quero agendar</a>
    </div>
  </section>
</main>

%(rodape)s

<a class="btn float" id="float" href="https://wa.me/5511982713543" target="_blank" rel="noopener" data-wa="barra"><span class="dot"></span>Agendar</a>

<div class="lb" id="lb" hidden>
  <img alt="">
  <button class="prev" aria-label="Foto anterior">&lsaquo;</button>
  <button class="next" aria-label="Pr\u00f3xima foto">&rsaquo;</button>
  <button class="x" aria-label="Fechar">&times;</button>
  <span class="lbcap"></span>
</div>

<script src="js/dados.js"></script>
<script src="js/main.js"></script>
</body>
</html>
""" % {'title': esc(pg['title']), 'desc': esc(pg['desc']), 'url': url,
       'ld': json.dumps(ld, ensure_ascii=False, indent=1),
       'nav': nav, 'rodape': rodape, 'curto': esc(_p.TITULOS_CURTOS[pg['slug']]),
       'eyebrow': esc(pg['eyebrow']), 'h1': esc(pg['h1']), 'lead': esc(pg['lead']),
       'blocos': '\n\n'.join(blocos), 'fotos': '\n        '.join(fotos),
       'gal_titulo': esc(gal_titulo), 'gal_nota': gal_nota,
       'duvidas': duvidas, 'irmas': irmas}


def gerar_paginas(alts):
    import paginas as _p
    idx = io.open(caminho('index.html'), encoding='utf-8').read()
    nav = pedaco(idx, '<header class="nav"', '</header>')
    rodape = pedaco(idx, '<footer>', '</footer>')
    # numa pagina interna, as ancoras do menu precisam voltar para a home
    nav_i = nav.replace('href="#', 'href="/#')
    rod_i = rodape.replace('href="#', 'href="/#')

    grafo = json.loads(pedaco(idx, '{\n "@context"', '\n}'))
    estudio = [n for n in grafo['@graph'] if n['@type'] == 'TattooParlor'][0]
    # na pagina interna basta a referencia, nao o no inteiro
    ref = {'@type': 'TattooParlor', '@id': estudio['@id'], 'name': estudio['name'],
           'url': estudio['url'], 'telephone': estudio['telephone'],
           'address': estudio['address'], 'aggregateRating': estudio['aggregateRating']}

    feitas = []
    for pg in _p.PAGINAS:
        io.open(caminho(pg['slug'] + '.html'), 'w', encoding='utf-8').write(
            pagina_html(pg, alts, nav_i, rod_i, ref))
        feitas.append(pg['slug'])
    return feitas


def main():
    trabalhos, duvidas = ler_dados()
    p = caminho('index.html')
    s = io.open(p, encoding='utf-8').read()
    s = trocar(s, 'galeria', html_galeria(trabalhos))
    s = trocar(s, 'duvidas', html_duvidas(duvidas))
    s = trocar(s, 'faq-schema',
               '<script type="application/ld+json">\n%s\n</script>' % jsonld_faq(duvidas))
    io.open(p, 'w', encoding='utf-8').write(s)
    print('index.html   %d fotos na galeria, %d duvidas, FAQ schema no HTML'
          % (len(trabalhos), len(duvidas)))

    alts = dict((o['img'], o) for o in trabalhos)
    feitas = gerar_paginas(alts)

    # links da home para as paginas de estilo, sempre em sincronia com paginas.py
    import paginas as _p
    links = '\n        '.join(
        '<a class="btn ghost" href="%s">%s</a>' % (x['slug'], esc(_p.TITULOS_CURTOS[x['slug']]))
        for x in _p.PAGINAS)
    s2 = io.open(caminho('index.html'), encoding='utf-8').read()
    s2 = trocar(s2, 'estilos', links)
    io.open(caminho('index.html'), 'w', encoding='utf-8').write(s2)
    print('index.html   %d links internos para as paginas de estilo' % len(_p.PAGINAS))
    for nome in feitas:
        print('%-28s gerada' % (nome + '.html'))

    io.open(caminho('sitemap.xml'), 'w', encoding='utf-8').write(sitemap(trabalhos))
    print('sitemap.xml  %d paginas + %d imagens' % (2 + len(feitas), len(trabalhos)))

if __name__ == '__main__':
    main()
