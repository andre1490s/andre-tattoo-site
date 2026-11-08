# Alterações de SEO — site André Tattoo

Registro do que foi modificado, por quê, e o que ainda falta.
Commit `ce07469` é o **marco zero**: cópia fiel do site como estava no ar em 08/11/2026.
Para reverter qualquer coisa: `git diff ce07469 -- <arquivo>`.

---

## Fase 1 — Home: título, H1 e dados estruturados

### 1.1 Title

| | |
|---|---|
| Antes | `Andre Tattoo · Realismo preto e cinza na Vila Matilde, São Paulo` |
| Depois | `Tatuador Realismo Preto e Cinza na Vila Matilde \| André Tattoo` |

**Por quê:** o título antigo começava pelo nome da marca. Quem já conhece a marca
acha o site de qualquer jeito; quem não conhece busca por *serviço + lugar*. O novo
começa por **"Tatuador Realismo Preto e Cinza"**, que é como a busca é digitada,
e deixa a marca no fim. 62 caracteres — cabe inteiro no resultado do Google.

### 1.2 Meta description

Agora cita **Zona Leste**, **retratos** e **coberturas** — três termos de busca que o
site atende mas não mencionava. 157 caracteres, dentro do limite de exibição.

### 1.3 H1

| | |
|---|---|
| Antes | `Transformando suas ideias em desenhos únicos.` |
| Depois | `Realismo em preto e cinza, feito sem pressa.` |

**Por quê, em três camadas:**

1. **Busca.** O H1 antigo não continha nenhuma palavra que alguém digita no Google.
   É o sinal mais forte de tema da página e estava desperdiçado. O novo abre com
   *realismo em preto e cinza* — o termo exato do posicionamento.
2. **Marca.** `contexto/marca.md` lista "único" entre os exageros a evitar. O H1
   antigo usava exatamente essa palavra.
3. **Voz.** "feito sem pressa" não é invenção: já era a frase da `og:description`
   do próprio site. Só foi promovida para o lugar onde tem peso.

Mantida a estrutura visual: 3 linhas, com a segunda parte em itálico dourado.
Testado em desktop (1280px) e iPhone 13 — sem quebra de layout, sem scroll horizontal.

### 1.4 Eyebrow (linha acima do H1)

`Tatuador na Vila Matilde, São Paulo` → `Tatuador na Vila Matilde · Zona Leste de São Paulo`

Acrescenta "Zona Leste", que é como muita gente da região se localiza.

### 1.5 Nome da marca padronizado

O site misturava **"Andre"** (logo, rodapé, texto do sobre, textos ALT) e
**"André"** (avaliações dos clientes, mensagens de WhatsApp). Para o Google,
inconsistência de nome enfraquece a identificação da entidade.

Padronizado para **"André"** em todo o texto visível. No schema ficou
`"alternateName": "Andre Tattoo"`, que declara ao Google que as duas grafias são
o mesmo negócio — nada se perde de quem busca sem acento.

> **Confirme:** o nome no seu Perfil da Empresa no Google deve bater com o do site.

### 1.6 Dados estruturados — reescritos

De **749** para **6.004** caracteres, reorganizados em `@graph` com três entidades
ligadas entre si:

**`TattooParlor` — o estúdio**
- `aggregateRating` — 5,0 com 228 avaliações
- `review` — 3 avaliações reais, copiadas do seu Perfil da Empresa
- `sameAs` — agora inclui o **Google**, além de Instagram e TikTok
- `hasOfferCatalog` — 7 serviços: realismo preto e cinza, retrato realista,
  cobertura, fechamento de braço, blackwork, fine line, realismo colorido
- `areaServed` — São Paulo, Zona Leste, Vila Matilde
- `hasMap`, `logo`, `availableLanguage`, `knowsAbout`
- `image` — 3 imagens em vez de 1

**`Person` — você**
Entidade própria para o André, ligada ao estúdio por `founder` e `employee`.
Serve para a busca por *"André tatuador"* e para IA entender que existe uma
pessoa por trás da marca.

**`WebSite`** — fecha o grafo e declara o idioma.

#### Ressalva honesta sobre as estrelas

O Google **não exibe estrelinhas** no resultado a partir de `aggregateRating`
declarado pelo próprio negócio: a política de *self-serving reviews* bloqueia isso
para `LocalBusiness`. Quem promete estrela com esse schema está te enganando.

O ganho real é outro: **compreensão de entidade e GEO**. É assim que ChatGPT,
Gemini e o AI Overview do Google entendem que você é 5,0 com 228 avaliações.
As estrelas que aparecem na busca continuam vindo do Perfil da Empresa.

---

## Pendências identificadas (ainda não corrigidas)

| # | O quê | Impacto | Fase |
|---|---|---|---|
| 1 | **Galeria sai só por JavaScript** — as 12 fotos não existem no HTML servido. O próprio site tem `<noscript>` admitindo. Fora do Google Imagens. | 🔴 alto | 2 |
| 2 | **FAQ schema também é injetado por JS** (`main.js:143`). Rastreadores de IA em geral não executam JavaScript — para eles, o FAQ não existe. | 🔴 alto | 2 |
| 3 | **Imagens sem `width`/`height`** — risco de CLS | 🟠 médio | 2 |
| 4 | **Textos ALT fracos** nas fotos do artista ("André tatuando um braço") | 🟠 médio | 2 |
| 5 | **Só 2 URLs** no site. Sem página de realismo, retrato, cobertura ou Zona Leste | 🔴 alto | 3 |
| 6 | **Sem GA4 e sem Search Console** — nada é medido hoje | 🔴 alto | 4 |
| 7 | **SVG de 47.878px** inline no HTML; **3 fontes externas** bloqueando render; vídeo `autoplay` no topo | 🟠 médio | 5 |
| 8 | **`postalCode` ausente** no schema — você precisa me passar o CEP | 🟡 baixo | — |
| 9 | **`geo` (lat/long) ausente** — não inventei coordenada; pode sair do seu Perfil da Empresa | 🟡 baixo | — |
| 10 | **Sobrenome do André** ausente no `Person` — hoje só "André" | 🟡 baixo | — |
| 11 | **Webhook em ngrok gratuito** (`dados.js`) — o endereço muda quando o n8n reinicia e os leads param de gravar | ⚠️ operacional | — |
| 12 | **No celular, o vídeo vem antes do H1** — o visitante vê a imagem antes de qualquer texto que explique o site | 🟠 CRO | 5 |

---

## Como testar localmente

```
cd andre-tattoo-site
python3 -m http.server 8099
```

Abra http://127.0.0.1:8099/ — o formulário não grava fora do servidor de produção,
mas todo o resto funciona igual.
