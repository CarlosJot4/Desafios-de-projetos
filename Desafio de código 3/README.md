# Phyton | Desafios de códigos | Segundo desafio (Identificando os Produtos Mais Vendidos)

## ✔Objetivo geral
Você está desenvolvendo um sistema para gerenciar dados de vendas que serão posteriormente importados para o Power BI. Você tem a estrutura de duas classes, Venda e Relatorio, já definidas. Sua tarefa é implementar partes específicas do código dentro dessas classes.

## ❗Detalhamento
1 - Classe Venda:

- Já está definida e contém as informações sobre uma venda, como produto, quantidade e valor.

2 - Classe Relatorio:

- Você precisa implementar o método adicionar_venda, que deve verificar se o objeto passado é uma instância da classe Venda antes de adicioná-lo à lista de vendas.

- ambém, no método calcular_total_vendas, você deve calcular o total de vendas multiplicando a quantidade pelo valor de cada venda adicionada ao relatório.

3 - Função main:

- Você deverá implementar a lógica para exibir o total de vendas utilizando o método calcular_total_vendas da classe Relatorio.

### ⬇Entrada
A entrada consiste em dados de vendas com as seguintes colunas:

- Produto (string)
- Quantidade (inteiro)
- Valor (decimal)

### ⬆Saída
A saída é o total de vendas calculado pela classe Relatorio.

### 💱Exemplo

| Entrada | Saída |
| -------- | ----- |
| Notebook
3
1500.00
Mouse
10
50.00
Teclado
5
100.00 | Total de Vendas: 5500.0 |
| Monitor
2
800.00
Webcam
1
120.00
Fone de Ouvido
4
75.00 | Total de Vendas: 2020.0 |
| Impressora
1
350.00
Cartucho
3
60.00
Scanner
2
200.00 | Total de Vendas: 930.0 |
