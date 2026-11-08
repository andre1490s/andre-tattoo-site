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
| 1 | ~~Galeria só por JavaScript~~ — **resolvido** pelo `build.py` | ✅ | 2 |
| 2 | ~~FAQ schema injetado por JS~~ — **resolvido**: agora está no HTML | ✅ | 2 |
| 3 | ~~Imagens sem `width`/`height`~~ — **resolvido**: lidos do arquivo pelo build | ✅ | 2 |
| 4 | ~~ALT fracos na galeria~~ — **4 reescritos** após olhar as fotos. Os das fotos do artista ("André tatuando um braço") seguem genéricos | 🟡 baixo | 5 |
| 5 | **Só 2 URLs** no site. Sem página de realismo, retrato, cobertura ou Zona Leste | 🔴 alto | 3 |
| 6 | **Sem GA4 e sem Search Console** — nada é medido hoje | 🔴 alto | 4 |
| 7 | **SVG de 47.878px** inline no HTML; **3 fontes externas** bloqueando render; vídeo `autoplay` no topo | 🟠 médio | 5 |
| 8 | ~~`postalCode` ausente~~ — **resolvido**: 03508-000 | ✅ | 1 |
| 9 | **`geo` (lat/long) ausente** — dispensável: com CEP completo + `hasMap` + `sameAs` do Perfil, o Google geocodifica sozinho | 🟡 baixo | — |
| 10 | ~~Sobrenome ausente~~ — **resolvido**: `Person` agora é "André Silva" | ✅ | 1 |
| 13 | **Contagem de avaliações fica velha sozinha** — está fixa em `dados.js`. Era 228, já são 230. Reconferir de vez em quando | 🟡 baixo | — |
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

---

## Fase 2 — Tirar a galeria e o FAQ de dentro do JavaScript

### O problema, em uma frase

As 12 fotos do portfólio e as 4 dúvidas **não existiam no HTML**. Eram criadas
por `js/main.js` depois que o navegador executava o JavaScript. O próprio site
admitia isso num `<noscript>`:

```html
<noscript><p>Para ver a galeria, ative o JavaScript...</p></noscript>
```

Quem lê a página sem executar JavaScript — **Google Imagens** e os rastreadores
de **ChatGPT, Gemini e Perplexity** — via uma caixa vazia. O portfólio, que é o
maior ativo comercial do site, estava fora do jogo.

### A solução: `build.py`

Um script que lê o `js/dados.js` e **grava** a galeria, as dúvidas e o JSON-LD do
FAQ dentro do `index.html`, entre marcadores:

```
python3 build.py
```

O `dados.js` continua sendo o único arquivo que você edita. O build só transforma
o que está lá em HTML de verdade.

### A rede de segurança

Se você editar o `dados.js` e **esquecer de rodar o build**, nada quebra. O
`main.js` compara quantas peças há no HTML com quantas há no `dados.js`:

- **Números iguais** → não mexe em nada. O HTML manda, e os rastreadores enxergam.
- **Números diferentes** → remonta a galeria sozinho, como fazia antes.

O site continua certo para quem visita; só volta a ficar invisível para os
rastreadores até o build rodar. **Testado:** removi uma peça do `dados.js` sem
rodar o build e a página renderizou as 11 restantes, sem erro.

O mesmo vale para o FAQ, com um cuidado a mais: o JSON-LD só é injetado pelo JS
se o build **não** tiver gravado antes — dois `FAQPage` na mesma página confundem
o Google.

### Também nesta fase

**`width` e `height` em todas as 12 fotos.** Lidos do arquivo real pelo build
(todas 3:4). Isso elimina o salto de layout enquanto a imagem carrega — o CLS do
Core Web Vitals.

**Sitemap de imagens.** O `sitemap.xml` agora declara as 12 fotos com título e
legenda, no padrão `image:image` do Google. É o caminho direto para o Google
Imagens descobrir o portfólio.

**4 textos ALT reescritos — depois de olhar cada foto, não de adivinhar:**

| Foto | Antes | Depois |
|---|---|---|
| `fera` | "Peça em blackwork com sombreado em pontilhismo" | "**Dragão** em blackwork com sombreado em pontilhismo no antebraço" |
| `rostos` | "Composição de rostos em realismo" | "Rostos de **estátuas gregas** em realismo preto e cinza, com efeito de **mármore partido**" |
| `retrato` | "Retrato realista no braço" | "Retrato masculino **de boné** em realismo preto e cinza no braço, com o **Cristo Redentor** abaixo" |
| `urso` | "Urso com lua e montanhas em realismo" | "Urso com lua e montanhas em realismo **preto e cinza**" |

A legenda visível de `fera` também mudou de "Blackwork · Pontilhismo" para
"Blackwork · Dragão". Os outros 8 ALT já eram bons e **não foram tocados** —
não há ganho em reescrever o que já descreve bem.

**`<noscript>` removido**, porque deixou de ser verdade.

### Testes executados

| Teste | Resultado |
|---|---|
| Fotos no HTML cru, sem JS | 12 ✓ |
| Dúvidas no HTML cru | 4 ✓ |
| `FAQPage` no HTML cru | sim ✓ |
| Duplicação com JS ligado | nenhuma — 12 fotos, 4 dúvidas, 2 blocos JSON-LD ✓ |
| Imagens sem `width`/`height` | 0 ✓ |
| Lightbox ao clicar na foto | abre com a imagem e a legenda certas ✓ |
| Acordeão do FAQ | abre um e fecha os outros ✓ |
| Rede de segurança (dados.js fora de sincronia) | remontou sozinho, sem erro ✓ |
| `build.py` rodado duas vezes | idempotente ✓ |
| Erros de console | nenhum ✓ |

### ⚠️ Mudança no seu fluxo de publicar tattoo nova

Antes: editar `js/dados.js` e publicar.
**Agora: editar `js/dados.js`, rodar `python3 build.py`, e publicar.**

Se esquecer, o site funciona igual — só perde o ganho de SEO daquela foto até
o build rodar. A skill `publicar-no-site`, no repositório `andre-tattoo-skill`,
precisa ser atualizada para incluir esse passo.

---

## Correção — descrições de tatuagem revertidas

Na fase 2 eu reescrevi 4 textos ALT olhando as fotos. O André corrigiu: a peça
`fera` **é um lobo, não um dragão**, e aquela foto é um close para mostrar o
detalhe do pontilhismo, não a peça inteira.

As 4 descrições voltaram ao que o André tinha escrito. **Lição registrada: não
interpretar o conteúdo das fotos.** Quem sabe o que cada peça é, e por que cada
foto foi enquadrada daquele jeito, é ele. As descrições das páginas novas usam
os textos do `dados.js` como estão, sem reinterpretação.

Única coisa que ficou do bloco de imagens da fase 2: `width`, `height` e o
sitemap — que são técnicos e não dependem de interpretar nada.

---

## Fase 4 — Medição (feita antes da 3, para as páginas novas já nascerem medidas)

O site não media **nada**: sem Analytics, sem Search Console, sem evento de
conversão. Era impossível dizer de onde vinha um cliente.

### Como ligar

Em `js/dados.js`, bloco `medicao`:

```js
medicao: { ga4: "" },
```

Cole o ID do Google Analytics (`G-XXXXXXXXXX`, em Admin → Fluxos de dados →
"ID da métrica") e pronto. **Enquanto estiver vazio, nada é baixado e nenhum
cookie é criado** — zero peso extra. Testado: com o campo vazio, zero
requisições ao Google e `dataLayer` nem existe.

### Eventos que passam a ser registrados sozinhos

| Evento | Quando | O que leva junto |
|---|---|---|
| `whatsapp_clique` | qualquer botão de WhatsApp | `lugar`: topo, obras, estudio, barra ou clube |
| `form_envio` | formulário de orçamento enviado | `origem` |
| `galeria_ampliar` | abriu uma foto | `peca` |
| `duvida_abrir` | abriu uma pergunta do FAQ | `pergunta` |

O `lugar` do `whatsapp_clique` é o que responde a pergunta que importa: **qual
parte da página traz cliente.** Se o botão do rodapé converte mais que o do
topo, isso muda o desenho da página.

### Search Console

A etiqueta de verificação ficou **comentada** no `<head>` do `index.html`, com o
passo a passo. Não dá para preencher sem a sua conta: o Google gera um código
único por propriedade.

---

## Fase 3 — Quatro páginas novas

O site tinha **2 URLs**. Passou a ter **6**.

| URL | Alvo de busca |
|---|---|
| `/realismo-preto-e-cinza` | tatuagem realismo preto e cinza, tatuador especialista em realismo |
| `/tatuagem-retrato-realista` | tatuagem de retrato realista, tatuagem de rosto, homenagem |
| `/cobertura-de-tatuagem` | cobertura de tatuagem, cover up, reforma de tatuagem |
| `/tatuador-zona-leste-sp` | tatuador zona leste, Penha, Tatuapé, Itaquera, Vila Matilde |

Cada uma tem: um H1 só, 4 seções de texto (450 a 540 palavras), galeria própria
selecionada do portfólio, 4 perguntas específicas, migalha de volta para a home,
links para as 3 páginas irmãs e CTA de WhatsApp no topo e no fim.

**Dados estruturados por página:** `BreadcrumbList` + `FAQPage` próprio +
`Service` + referência ao estúdio pelo `@id`, ligando tudo ao grafo da home.

A home ganhou uma seção **"O que eu faço"** com links para as quatro — os links
são gerados pelo build, então nunca saem de sincronia.

### O conteúdo

Escrito respeitando `contexto/marca.md`: **nenhum preço**, nenhuma faixa, nenhum
"a partir de"; nada de "único" ou "exclusivo"; nenhum número de clientes, tempo
de carreira ou prêmio inventado; maori não aparece.

O que sustenta cada página é informação verdadeira que o André já pratica: a
política de sinal, retoque a partir de 40 dias, 18 anos com documento, um
trabalho grande por dia, material descartável aberto na frente do cliente,
desenho feito depois da data marcada.

Nenhuma página promete resultado, e a de cobertura diz abertamente que **às
vezes a resposta é não** — o que é diferença real em relação aos concorrentes.

### Bug encontrado e corrigido no caminho

As quatro páginas apareciam com **12 fotos** em vez das 6, 4, 3 e 6 escolhidas.
A rede de segurança da fase 2 estava substituindo a galeria curada pela lista
inteira do `dados.js`, porque os números não batiam.

Correção: o contêiner agora declara de onde vem o conteúdo.
`data-fonte="dados"` na home (compara com o `dados.js` e remonta se houver
diferença) e `data-fonte="pagina"` nas páginas de estilo (o JS não toca). Mesma
lógica para o FAQ.

### Testes executados

| Teste | Resultado |
|---|---|
| Um H1 por página | 4/4 ✓ |
| Galeria com a seleção certa | 6, 4, 3, 6 ✓ |
| Imagens sem `width`/`height` | 0 ✓ |
| JSON-LD por página | Breadcrumb + FAQ + Service + estúdio ✓ |
| Canonical correto | 4/4 ✓ |
| Links internos por página | 4 ✓ |
| Home ainda com 12 fotos | ✓ |
| Lightbox e acordeão | ✓ |
| Scroll horizontal no celular | nenhum ✓ |
| Erros de console | nenhum ✓ |
| Medição sem ID | 0 requisições, sem cookie ✓ |
| Medição com ID | gtag carregado, 4 eventos disparando ✓ |

### Também nesta fase

`clube-15.html` passou a escrever **André** com acento (título, OG, logo e
rodapé), igual ao resto do site.

### ⚠️ Conferir antes de publicar

A página da Zona Leste afirma que **a Vila Matilde é atendida pela Linha
3-Vermelha do metrô** e que **há estacionamento na rua**. Escrevi a partir do
endereço, mas quem conhece o bairro é você: confirme as duas frases.

---

## Adendo — dados confirmados pelo Perfil da Empresa (08/11/2026)

Print do painel do Google enviado pelo André trouxe três correções:

**CEP: 03508-000.** Adicionado ao `postalCode`. Endereço completo no schema agora
bate exatamente com o do Perfil da Empresa.

**O Perfil da Empresa se chama "Studio Andre Tattoo"** — não "André Tattoo".
Tratamento: o site continua com a marca **André Tattoo** (é o que está no logo e no
manual de marca), e o schema declara as três grafias:

```
"name": "André Tattoo"
"alternateName": ["Andre Tattoo", "Studio Andre Tattoo"]
```

> **Decisão consciente de NÃO mexer no Perfil da Empresa.** Trocar o nome de um
> perfil com 230 avaliações pode cair em revisão manual do Google e derrubar a
> posição no mapa por semanas. O ganho de ter o nome idêntico é pequeno perto
> desse risco — e o `sameAs` apontando para o Perfil já é um elo mais forte do
> que a coincidência exata de nome.

**230 avaliações, não 228.** Corrigido no `dados.js` e no schema. Esse número é
fixo no arquivo e envelhece sozinho: vale reconferir a cada poucas semanas.

**Sobre o nome "André Silva":** o André comentou que é um nome muito comum e que
não tem nome artístico. Na prática ele já tem: **"André Tattoo"** é o nome pelo
qual é buscado, e está no logo, no domínio, no Instagram e no Perfil da Empresa.
Foi registrado no schema como `Person.name: "André Silva"` com
`alternateName: "André Tattoo"` — que é o que o Google usa para ligar a pessoa
à marca. Não há nada a resolver aqui.

### Oportunidades que apareceram no painel do Perfil

| O que o painel mostra | Ação |
|---|---|
| 350 interações com clientes | Base para comparar depois que o SEO entrar |
| "Receba um link personalizado e QR code para convidar clientes a avaliar" | **Usar.** É a forma legítima de crescer as avaliações — gerar o link e mandar para quem já tatuou |
| Botão "Agendar on-line" ativo no perfil | Conferir para onde aponta: o ideal é o WhatsApp ou o site, com parâmetro de origem para dar para medir |
| "Adicione um mapa ao seu site" | O site já tem link para o mapa; um mapa incorporado é opcional e pesa na performance. Avaliar na fase 5 |

---

## Correção antes de ligar a Netlify ao repositório — `404.html`

O André testou `andretattoo.com.br/realismo-preto-e-cinza`, viu o 404 e mandou o
print. O 404 em si era esperado (a Netlify ainda não estava ligada ao
repositório), **mas o print revelou outra coisa:** o site tem uma página 404
customizada — "Linha perdida / 404" — que **não estava no repositório**.

Por que escapou: eu montei a cópia do site seguindo os links de cada arquivo, e
**nada no site aponta para o `404.html`**. Ele só aparece quando o servidor não
acha o endereço.

Se a Netlify tivesse sido ligada ao repositório antes dessa correção, essa página
teria sumido e dado lugar ao 404 genérico da Netlify.

### Varredura feita depois disso

Procurei todos os arquivos que costumam existir sem estar linkados:

| Arquivo | Existe no site? |
|---|---|
| `404.html` | **sim** — faltava, foi acrescentado |
| `_redirects`, `_headers`, `netlify.toml` | não |
| `manifest.json`, `site.webmanifest` | não |
| `favicon.ico`, `humans.txt`, `browserconfig.xml`, `ads.txt` | não |

E conferi que toda referência de todo HTML, CSS e JS aponta para um arquivo que
existe no repositório: **nenhuma quebrada**.

O `404.html` já tinha `noindex`, que é o correto. Só padronizei a marca para
"André" no título, como no resto do site.
