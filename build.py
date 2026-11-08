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
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
            '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
            '  <url>\n    <loc>https://andretattoo.com.br/</loc>\n'
            '    <lastmod>%s</lastmod>\n    <changefreq>monthly</changefreq>\n'
            '    <priority>1.0</priority>\n%s\n  </url>\n'
            '  <url>\n    <loc>https://andretattoo.com.br/clube-15</loc>\n'
            '    <lastmod>%s</lastmod>\n    <changefreq>monthly</changefreq>\n'
            '    <priority>0.8</priority>\n  </url>\n</urlset>\n' % (hoje, imgs, hoje))

def main():
    trabalhos, duvidas = ler_dados()
    p = caminho('index.html')
    s = io.open(p, encoding='utf-8').read()
    s = trocar(s, 'galeria', html_galeria(trabalhos))
    s = trocar(s, 'duvidas', html_duvidas(duvidas))
    s = trocar(s, 'faq-schema',
               '<script type="application/ld+json">\n%s\n</script>' % jsonld_faq(duvidas))
    io.open(p, 'w', encoding='utf-8').write(s)
    io.open(caminho('sitemap.xml'), 'w', encoding='utf-8').write(sitemap(trabalhos))
    print('index.html   %d fotos na galeria, %d duvidas, FAQ schema no HTML' % (len(trabalhos), len(duvidas)))
    print('sitemap.xml  2 paginas + %d imagens' % len(trabalhos))

if __name__ == '__main__':
    main()
