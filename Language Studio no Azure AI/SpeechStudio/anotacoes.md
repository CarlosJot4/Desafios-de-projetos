### Speech Studio – Anotações

## Speech-to-Text

# Experimento:

 - Testado com 2 arquivos de áudio:

    1. Voz clara e sem ruído
    2. Voz com ruído de fundo (trânsito)


# Observações:

 - Alta precisão com voz clara.
 - Queda leve na qualidade com ruído, mas ainda compreensível.
 - Mesmo com sotaque a voz foi reconhecido com sucesso, porém algumas palavras específicas foram mal interpretadas.

## Text-to-Speech

# Experimento:

Geração de fala com texto curto: “Olá, tudo bem? Este é um teste.”

 - Vozes testadas:

    1. pt-BR Francisca (neural)
    2. pt-BR Antônio (neural)

# Observações:

 - A voz neural tem entonação natural e fluida.
 - Pode-se usar comandos para alterar o tom, velocidade e pausas.

## Custom Speech

# Experimento:

Criado modelo personalizado com termos técnicos da área da saúde.

# Observações:

 - Após treinamento, o reconhecimento de vocabulário técnico melhorou significativamente.
 - Processo de treinamento é simples, mas requer amostra bem definida de áudio e transcrição.

## Conclusões Parciais:

 - Speech Studio é poderoso para construir aplicações acessíveis, como leitores de tela e assistentes virtuais.
 - Custom Speech pode ser essencial para domínios técnicos ou linguagens específicas.