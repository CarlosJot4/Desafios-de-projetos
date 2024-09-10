# Phyton | Desafios de códigos | Quarto desafio (Explorando Técnicas de POO com Python 2)

## ✔Objetivo geral
Você está desenvolvendo um sistema para organizar vendas por categorias antes de gerar um relatório. O objetivo é criar uma classe Categoria que gerencie as vendas associadas a uma determinada categoria e calcule o total de vendas dessa categoria.

## ❗Detalhamento
1 - Método adicionar_venda: Na classe Categoria, crie um método chamado adicionar_venda que adiciona um objeto Venda à lista de vendas da categoria.

2 - Método total_vendas: Na classe Categoria, crie um método chamado total_vendas que calcula e retorna o total das vendas (soma do valor de todas as vendas) para essa categoria.

3 - Função main:

| Entrada de Dados | Implementação |
| ---------------- | ------------- |
|Leia o nome das categorias e, para cada categoria, leia as vendas associadas.|Adicione cada venda à categoria correspondente usando o método adicionar_venda|
|Exiba o total de vendas para cada categoria|Utilize o método total_vendas para calcular e exibir o total das vendas|

### ⬇Entrada
A entrada consiste em:

- Nome da Categoria (string)
- Lista de Vendas (com as colunas Produto, Quantidade, Valor

### ⬆Saída
A saída é o total de vendas por categoria.

### 💱Exemplo

| Entrada | Saída |
| -------------- | ------------ |
| Eletrônicos
Celular, 5, 1000
Fone de Ouvido, 10, 500
Móveis
Mesa, 2, 800 | Vendas em Eletrônicos: 1500.0 |
Cadeira, 4, 400 | Vendas em Móveis: 1200.0 |
| -------------- | ------------ |
| Alimentos
Arroz, 10, 200
Feijão, 7, 140
Jardinagem
Planta, 2, 60 | Vendas em Alimentos: 340.0 |
Ferramentas, 1, 100 | Vendas em Jardinagem: 160.0 |
| -------------- | ------------ |
| Livros
Aventuras no Tempo, 1, 80
Mistérios do Oceano, 2, 90
Esportes
Tênis, 7, 210 | Vendas em Livros: 170.0 |
Bola, 3, 120 | Vendas em Esportes: 330.0 |
