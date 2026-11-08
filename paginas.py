# -*- coding: utf-8 -*-
"""
Conteudo das paginas de estilo. O build.py le daqui e gera os .html.

REGRAS QUE ESTE TEXTO RESPEITA (contexto/marca.md):
  - nenhum preco, nenhuma faixa, nenhum "a partir de"
  - nada de "unico", "exclusivo", "melhor do Brasil"
  - nenhum numero de clientes, tempo de carreira ou premio inventado
  - nenhuma escassez falsa
  - maori nao e oferecido
"""

PAGINAS = [

{
 "slug": "realismo-preto-e-cinza",
 "title": "Tatuagem em Realismo Preto e Cinza em São Paulo | André Tattoo",
 "desc": "Tatuagem em realismo preto e cinza na Vila Matilde, São Paulo. Projeto autoral desenhado para o seu corpo, em sessão com hora marcada. Veja trabalhos e agende.",
 "eyebrow": "Realismo preto e cinza",
 "h1": "Realismo em preto e cinza",
 "lead": "O estilo que o estúdio faz todo dia: luz, sombra e profundidade construídas "
         "sem cor, pensando em como a peça vai estar daqui a dez anos.",
 "servico": "Tatuagem em realismo preto e cinza",
 "blocos": [
   ("O que é realismo em preto e cinza", [
     "Realismo preto e cinza é tatuar sem cor nenhuma: o volume inteiro da peça vem "
     "da diferença entre as áreas claras e escuras. Onde uma tatuagem colorida resolve "
     "com tinta, essa resolve com sombra — e é por isso que ela depende tanto de "
     "planejamento. A luz precisa vir de um lugar só, e cada parte do desenho tem que "
     "obedecer a essa decisão.",
     "Na prática, o que você vê de perto é uma transição suave entre cinzas. O que você "
     "vê de longe é a forma: um rosto, um animal, uma peça de mármore. Quando o "
     "planejamento está certo, a peça funciona nas duas distâncias."
   ]),
   ("Por que preto e cinza envelhece bem", [
     "Toda tatuagem clareia com o tempo. A diferença é que, no preto e cinza, o que "
     "clareia é a mesma tinta em intensidades diferentes — então a peça perde contraste "
     "de forma uniforme, e o desenho continua legível. Peças muito coloridas tendem a "
     "perder cada pigmento num ritmo, e o conjunto desmonta antes.",
     "Isso não significa que preto e cinza não precise de cuidado. Significa que, com "
     "cuidado parecido, ela costuma pedir menos manutenção ao longo dos anos. É um dos "
     "motivos de o estúdio ter escolhido esse foco."
   ]),
   ("Como o projeto é feito aqui", [
     "Nada é catálogo. Você manda a ideia, a região do corpo e as referências, e o "
     "desenho nasce em cima disso. O corpo manda na composição: a mesma ideia num "
     "antebraço e numa panturrilha vira duas peças diferentes, porque o espaço, a "
     "curvatura e o sentido de leitura mudam.",
     "O desenho é feito depois da data marcada e você vê antes da sessão. Ajuste faz "
     "parte: mexemos no que for preciso antes de aplicar o stencil. O que não dá é "
     "redesenhar o projeto inteiro com você já na cadeira.",
     "No dia, é um trabalho grande por vez. Material descartável aberto na sua frente, "
     "ambiente reservado e pausa sempre que precisar."
   ]),
   ("Onde o realismo rende mais", [
     "Antebraço, braço, panturrilha e costas são as regiões que mais aproveitam o "
     "estilo: são superfícies grandes o bastante para a sombra respirar. Em áreas "
     "pequenas, o realismo perde — detalhe demais em espaço de menos vira borrão com "
     "o passar dos anos.",
     "Se a sua ideia é grande e o espaço é pequeno, eu falo isso antes, na avaliação. "
     "É melhor ajustar o tamanho ou escolher outro lugar do corpo do que entregar uma "
     "peça que não vai durar."
   ]),
 ],
 "galeria": ["justica", "poseidon", "leao", "arcanjo", "cigana", "retrato-oculos"],
 "faq": [
   ("Quantas sessões leva uma peça em realismo?",
    "Depende do tamanho e da densidade de sombra. Peças de antebraço costumam sair em "
    "uma ou duas sessões; fechamentos de braço e costas são planejados por etapas. Na "
    "avaliação eu digo quantas sessões o seu projeto pede, antes de qualquer combinado."),
   ("Realismo dói mais que outros estilos?",
    "O que define a dor é a região do corpo e o tempo de sessão, não o estilo. Realismo "
    "costuma pedir sessões mais longas pela quantidade de sombreado, e é por isso que a "
    "sessão tem pausa sempre que você precisar."),
   ("Dá para fazer realismo pequeno?",
    "Dá, mas com limite. Realismo precisa de espaço para a transição de sombra existir. "
    "Em peças muito pequenas o detalhe se fecha com o tempo e o desenho perde a leitura. "
    "Prefiro ajustar a escala na avaliação a entregar algo que não envelhece bem."),
   ("O estúdio faz realismo colorido também?",
    "Faz. O foco é preto e cinza, mas peças em realismo colorido fazem parte do "
    "trabalho — é só me contar o que você imagina."),
 ],
 "irmas": ["tatuagem-retrato-realista", "cobertura-de-tatuagem", "tatuador-zona-leste-sp"],
},

{
 "slug": "tatuagem-retrato-realista",
 "title": "Tatuagem de Retrato Realista em São Paulo | André Tattoo",
 "desc": "Tatuagem de retrato realista na Vila Matilde, São Paulo. Retrato de pessoa ou pet a partir da sua foto, em preto e cinza. Mande a referência e receba a avaliação.",
 "eyebrow": "Retrato realista",
 "h1": "Tatuagem de retrato realista",
 "lead": "O trabalho mais difícil do realismo e o mais pessoal: a pele de alguém "
         "carregando o rosto de alguém.",
 "servico": "Tatuagem de retrato realista",
 "blocos": [
   ("A foto decide metade do resultado", [
     "Retrato é o único trabalho em que a referência manda tanto quanto a mão. Uma foto "
     "com luz definida — onde dá para ver de onde vem a claridade e onde a sombra cai — "
     "permite construir volume de verdade. Uma foto achatada, de flash direto ou muito "
     "pequena, não tem a informação necessária: o que falta na imagem não tem como "
     "aparecer na pele.",
     "O que ajuda: resolução alta, rosto grande no quadro, luz lateral, expressão "
     "natural. O que atrapalha: foto de foto, print de rede social, imagem escura, "
     "muito recorte ou filtro pesado.",
     "Se a única foto que existe é ruim — e às vezes é, porque é a foto que sobrou — me "
     "mande assim mesmo. Eu digo honestamente o que dá e o que não dá para reconstruir, "
     "antes de você decidir qualquer coisa."
   ]),
   ("Homenagem", [
     "Boa parte dos retratos que faço são de pai, mãe, avó, filho ou de alguém que já "
     "morreu. É um trabalho que pede um tipo de cuidado diferente: a pessoa não está "
     "escolhendo um desenho, está escolhendo como vai carregar alguém.",
     "Por isso a conversa vem antes da agulha. Eu quero saber quem é, o que essa pessoa "
     "representa e o que você quer que o retrato transmita — se é o olhar, o sorriso, "
     "um gesto. Isso muda a escolha da foto, o enquadramento e até o tamanho."
   ]),
   ("Tamanho não é detalhe", [
     "Retrato pequeno é o pedido que eu mais preciso ajustar. Um rosto carrega "
     "informação em escala minúscula: a pálpebra, o canto da boca, a sombra abaixo do "
     "nariz. Quando a peça é pequena demais, esses pontos se fecham com a cicatrização "
     "e, alguns anos depois, o rosto deixa de ser aquela pessoa.",
     "Antebraço, braço e panturrilha são as regiões que mais funcionam. Na avaliação eu "
     "falo o tamanho mínimo para o seu retrato específico — depende do rosto, não de uma "
     "regra fixa."
   ]),
   ("Retrato de pet", [
     "Vale a mesma lógica, com uma diferença: pelo. Construir textura de pelo em preto e "
     "cinza é trabalhoso e é justamente o que faz o bicho parecer ele mesmo, e não um "
     "cachorro genérico. Fotos com boa luz, de frente ou três quartos, e com o focinho "
     "nítido, são as que mais rendem.",
     "Pet também é um dos trabalhos que mais fazemos em realismo colorido, quando a cor "
     "é parte do que identifica o animal."
   ]),
 ],
 "galeria": ["retrato-oculos", "retrato", "rostos", "pet"],
 "faq": [
   ("Que tipo de foto devo mandar para um retrato?",
    "De preferência uma foto com boa resolução, com o rosto grande no quadro e com luz "
    "lateral, que mostre de onde vem a claridade. Evite print de rede social, foto de "
    "foto, imagem escura ou com filtro pesado. Se a foto que você tem é a única que "
    "existe, mande assim mesmo e eu digo o que é possível."),
   ("Dá para fazer retrato de quem já faleceu?",
    "Dá, e é uma parte grande do trabalho. O que decide é a qualidade da referência. "
    "Mande a melhor foto que existir e, se houver mais de uma, mande todas: às vezes "
    "uma resolve a luz e outra resolve a expressão."),
   ("Qual o tamanho mínimo de um retrato?",
    "Não existe número fixo, porque depende do rosto e da quantidade de detalhe. O que "
    "existe é um limite: abaixo de certo tamanho o detalhe fecha com o tempo e o rosto "
    "deixa de ser reconhecível. Eu falo o mínimo do seu caso na avaliação."),
   ("Retrato precisa de retoque?",
    "A regra é a mesma de qualquer peça: a partir de 40 dias da sessão, se for "
    "necessário, depois de eu avaliar por foto ou pessoalmente. Falha na aplicação, "
    "retoque sem custo."),
 ],
 "irmas": ["realismo-preto-e-cinza", "cobertura-de-tatuagem", "tatuador-zona-leste-sp"],
},

{
 "slug": "cobertura-de-tatuagem",
 "title": "Cobertura de Tatuagem (Cover-Up) em São Paulo | André Tattoo",
 "desc": "Cobertura de tatuagem antiga na Vila Matilde, Zona Leste de São Paulo. Mande uma foto da peça atual e receba uma avaliação honesta do que dá para cobrir.",
 "eyebrow": "Cobertura e reforma",
 "h1": "Cobertura de tatuagem",
 "lead": "Aquela tatuagem que você não gosta mais não precisa continuar assim — "
         "mas cobertura tem regra, e é melhor saber antes.",
 "servico": "Cobertura de tatuagem (cover-up)",
 "blocos": [
   ("Cobertura não apaga: reorganiza", [
     "A primeira coisa a entender é que tinta não sai com tinta. Uma cobertura não "
     "remove o desenho antigo — ela constrói um desenho novo que usa as áreas escuras "
     "que já existem como sombra, e esconde o resto dentro da composição.",
     "Por isso cobertura quase sempre fica maior e mais escura que a peça original. É a "
     "física do trabalho, não preferência: para apagar visualmente uma linha preta, "
     "você precisa de algo igual ou mais denso em volta dela."
   ]),
   ("O que é fácil, o que é difícil e o que não dá", [
     "Peças antigas, desbotadas, de traço fino e em tons médios são as mais fáceis: "
     "sobra espaço para desenhar por cima. Realismo preto e cinza funciona bem como "
     "cobertura justamente porque trabalha com massa de sombra.",
     "Difícil é cobrir preto sólido, contorno muito grosso ou peça recente e saturada. "
     "Nesses casos, muitas vezes a resposta certa é clarear antes, com algumas sessões "
     "de remoção a laser em outro profissional, e só depois tatuar. Clarear não é "
     "apagar: bastam algumas sessões para abrir espaço, não é preciso sumir com tudo.",
     "E tem o caso em que a resposta honesta é não. Se o que você quer por cima não "
     "cabe no que está lá, eu falo — prefiro perder o trabalho a entregar uma cobertura "
     "que você vai querer cobrir de novo."
   ]),
   ("Como funciona a avaliação", [
     "Mande pelo WhatsApp uma foto da tatuagem atual com boa luz natural, de frente, "
     "sem filtro e sem flash direto. Se a peça for grande ou curvar no corpo, mande "
     "mais de um ângulo.",
     "Com isso eu digo três coisas: o que dá para esconder, se vale clarear antes e "
     "quais tipos de desenho funcionam naquele formato. Só depois disso a gente fala de "
     "projeto e data."
   ]),
   ("Reforma é outra coisa", [
     "Nem todo caso é cobertura. Às vezes a peça é boa e só perdeu contraste com o "
     "tempo: aí o trabalho é reforço de sombra e contorno, mantendo o desenho original. "
     "Outras vezes dá para ampliar, integrando o que existe a uma composição maior em "
     "vez de esconder.",
     "Na foto já dá para dizer em qual dos três caminhos o seu caso está."
   ]),
 ],
 "galeria": ["justica", "arcanjo", "cigana"],
 "galeria_titulo": "Trabalhos em preto e cinza",
 "galeria_nota": "Peças do portfólio em preto e cinza — o mesmo tipo de construção de "
                 "sombra que uma cobertura usa. Exemplos de cobertura eu mando no "
                 "WhatsApp, junto com a avaliação do seu caso.",
 "faq": [
   ("Dá para cobrir qualquer tatuagem?",
    "Não. Peças desbotadas, de traço fino e em tons médios são as mais fáceis. Preto "
    "sólido, contorno muito grosso ou tatuagem recente e saturada podem exigir clareamento "
    "a laser antes. Mande uma foto com boa luz e eu digo com honestidade o que é possível."),
   ("Preciso remover a tatuagem antes?",
    "Nem sempre. Quando é preciso, na maioria das vezes bastam algumas sessões de laser "
    "para clarear e abrir espaço — não é necessário apagar tudo. Isso é feito com um "
    "profissional de remoção; eu indico o caminho e depois faço o trabalho."),
   ("A cobertura fica maior que a tatuagem antiga?",
    "Quase sempre, sim. Para esconder o que já está na pele, o desenho novo precisa de "
    "margem em volta e de áreas escuras onde apoiar a composição. Isso é dito antes, "
    "junto com o projeto."),
   ("Qual foto devo mandar da tatuagem que quero cobrir?",
    "Luz natural, de frente, sem filtro e sem flash direto. Se a peça for grande ou "
    "contornar o corpo, mande mais de um ângulo."),
 ],
 "irmas": ["realismo-preto-e-cinza", "tatuagem-retrato-realista", "tatuador-zona-leste-sp"],
},

{
 "slug": "tatuador-zona-leste-sp",
 "title": "Tatuador na Zona Leste de São Paulo · Vila Matilde | André Tattoo",
 "desc": "Estúdio de tatuagem na Vila Matilde, Zona Leste de São Paulo. Realismo preto e cinza com hora marcada, em ambiente reservado. Av. Melchert, 606. Agende pelo WhatsApp.",
 "eyebrow": "Vila Matilde · Zona Leste",
 "h1": "Tatuador na Zona Leste de São Paulo",
 "lead": "O estúdio fica na Vila Matilde, e o atendimento é um de cada vez, "
         "com hora marcada.",
 "servico": "Estúdio de tatuagem na Vila Matilde",
 "blocos": [
   ("Onde fica", [
     "Av. Melchert, 606 — Vila Matilde, São Paulo (SP), CEP 03508-000. É um estúdio de "
     "rua na Zona Leste, não uma sala dentro de um prédio comercial: você chega, toca e "
     "entra.",
     "A Vila Matilde é atendida pela Linha 3-Vermelha do metrô, o que facilita para "
     "quem vem de outras regiões da cidade sem carro."
   ]),
   ("Quem costuma vir aqui", [
     "A maior parte dos clientes vem dos bairros vizinhos — Penha, Tatuapé, Itaquera, "
     "Artur Alvim, Carrão, Guaianases, Cangaíba, Vila Esperança, Vila Formosa — mas "
     "também recebo gente de outras zonas de São Paulo e de cidades do ABC e da Grande "
     "São Paulo, porque projeto grande em realismo não se escolhe pela distância.",
     "Como é um trabalho grande por dia, quem vem de longe consegue resolver a peça em "
     "sessão cheia, em vez de parcelar em várias viagens curtas."
   ]),
   ("Como é o atendimento", [
     "Só com hora marcada. Não há fila, não há espera e não há outra pessoa sendo "
     "tatuada ao mesmo tempo: naquele turno o estúdio é seu.",
     "Agulhas e insumos descartáveis são abertos na sua frente, a cada sessão. O "
     "ambiente é reservado, e você pode trazer um acompanhante. Sessão longa tem pausa "
     "— é só pedir.",
     "O atendimento é de segunda a sábado, das 9h às 22h. Só atendo a partir dos 18 "
     "anos, com documento com foto no dia, sem exceção e sem autorização dos pais."
   ]),
   ("Antes de vir", [
     "A conversa começa no WhatsApp: você manda a ideia, a região do corpo, o tamanho "
     "que imagina e as referências. Eu avalio, falo o que a região comporta e passo o "
     "valor pessoalmente — orçamento não sai por tabela nem por robô.",
     "Com o combinado fechado, o sinal reserva a sua data. Ele é abatido na sessão e "
     "não é devolvido em cancelamento ou reagendamento, porque aquele dia sai da agenda "
     "e não volta a ser vendido. Tudo isso é dito antes de qualquer cobrança."
   ]),
 ],
 "galeria": ["justica", "poseidon", "leao", "cigana", "raposa", "urso"],
 "faq": [
   ("Onde fica o estúdio e qual o horário?",
    "Av. Melchert, 606, Vila Matilde, São Paulo (SP), CEP 03508-000. Atendimento de "
    "segunda a sábado, das 9h às 22h, somente com hora marcada."),
   ("Precisa agendar ou posso aparecer?",
    "Precisa agendar. Como é um trabalho grande por dia e o estúdio atende uma pessoa "
    "por vez, não há atendimento sem hora marcada."),
   ("Atende quem é de outros bairros ou de fora de São Paulo?",
    "Sim. A maior parte vem dos bairros vizinhos da Zona Leste, mas recebo gente de "
    "outras zonas da cidade, do ABC e da Grande São Paulo. Quem vem de longe costuma "
    "resolver a peça em sessão cheia."),
   ("Menor de 18 anos pode tatuar?",
    "Não. O estúdio não atende menores de 18 anos, com ou sem autorização dos pais. É "
    "necessário documento com foto no dia da sessão."),
 ],
 "irmas": ["realismo-preto-e-cinza", "tatuagem-retrato-realista", "cobertura-de-tatuagem"],
},

]

TITULOS_CURTOS = {
 "realismo-preto-e-cinza":   "Realismo preto e cinza",
 "tatuagem-retrato-realista":"Retrato realista",
 "cobertura-de-tatuagem":    "Cobertura de tatuagem",
 "tatuador-zona-leste-sp":   "Tatuador na Zona Leste",
}
