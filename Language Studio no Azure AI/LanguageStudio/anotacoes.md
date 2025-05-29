# Language Studio – Anotações

## Análise de Sentimentos

### Experimento:

Analisado 5 textos com polaridades diferentes:

    - Positivo simples
    - Positivo com sarcasmo
    - Neutro
    - Negativo direto
    - Negativo subjetivo

### Observações:

 - Funciona bem com textos simples e diretos.
 - Apresenta dificuldades em identificar sarcasmo e ironia.
 - Classificações geralmente confiáveis quando o texto é mais claro.

## Extração de Entidades (NER)

### Experimento:

Aplicado a uma notícia jornalística e a um relatório técnico.

### Observações:

 - Boa identificação de entidades como nomes próprios, organizações, locais e datas.
 - Termos técnicos foram ignorados em alguns casos.

## Classificação de Texto

### Experimento:

Criado modelo para classificar textos como:

    - Informativo
    - Publicitário
    - Opinativo

### Observações:

 - Após o treinamento supervisionado com exemplos curtos, o modelo classificou corretamente 80% dos casos de teste.
 - Mais dados melhorariam a precisão.

## Sumarização de Texto

### Experimento:

Utilizado um artigo de blog de 800 palavras.

### Observações:

 - O resumo foi coeso e relevante.
 - Reduziu o texto em cerca de 70% mantendo o sentido principal.
 - Algumas nuances foram perdidas, como opiniões subjetivas.

## Conclusões Parciais:

 - Language Studio é eficiente para tarefas de processamento de linguagem natural comuns.
 - Pode ser integrado em fluxos de trabalho como análise de reviews, categorização de e-mails e geração de insights de textos longos.
