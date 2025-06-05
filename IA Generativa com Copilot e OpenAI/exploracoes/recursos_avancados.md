# exploracoes/recursos\_avancados.md

## Recursos Avançados Testados

### 🔧 Parâmetros de Geração

* **Temperature**: valores entre 0.2 e 0.8 testados. Valores baixos resultaram em respostas mais diretas e conservadoras.
* **Max Tokens**: definido entre 50 a 200, dependendo do tamanho esperado da resposta.
* **Stop Sequences**: usadas para limitar saídas em diálogos ou listas.

### 🔍 Prompt Engineering

* Prompts com instruções específicas ("resuma como um professor universitário", "crie em formato de tabela") produzem respostas mais refinadas.
* Uso de *shots* (exemplos anteriores) para dar contexto e orientar o tom da resposta.

### ⚙️ Integração com API

* Exploradas chamadas via `openai.ChatCompletion.create()` com logs de uso e custo.
* Ferramentas como Postman e scripts Python utilizados para testar requisições.

### 🔒 Moderação de Conteúdo

* Compreendido o funcionamento das camadas de filtragem por categorias sensíveis (ódio, violência, etc.).
* Testes com conteúdo neutro e limítrofe mostraram a atuação dos filtros de segurança em tempo real.
