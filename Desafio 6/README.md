# Phyton | Desafio de modelagem | Sexto desafio (Modelagem e Transformação de dados com DAX com Power BI)

## ✔Objetivo geral
Utilizaremos a tabela única de Financial Sample para criar as tabelas dimensão e fato do nosso modelo baseado em star schema.

## ❗Detalhamento
O processo consiste na criação das tabelas com base na tabela original. A partir da cópia serão selecionadas as colunas que irão compor a visão da nova tabela. Sendo assim, a partir da tabela principal serão criadas as tabelas:

 - Financials_origem (modo oculto – backup)
 - D_Produtos (ID_produto, Produto, Média de Unidades Vendidas, Médias do valor de vendas, Mediana do valor de vendas, Valor máximo de Venda, Valor mínimo de Venda)
 - D_Produtos_Detalhes(ID_produtos, Discount Band, Sale Price, Units Sold, Manufactoring Price)
 - D_Descontos (ID_produto, Discount, Discount Band)
 - D_Detalhes (*)
 - D_Calendário – Criada por DAX com calendar()
 - F_Vendas (SK_ID , ID_Produto, Produto, Units Sold, Sales Price, Discount Band, Segment, Country, Salers, Profit, Date (campos))

Verifique as informações que não foram contempladas nas demais tabelas dimensão que fornecem maiores detalhes sobre vendas
Criar tabela por agrupamento das informações.
Criar coluna a partir de condicional – Índice de Produto
Reorganizar as colunas


## 💥Desafio

 - Salve o projeto .pbix:
  [Arquivo do PowerBI]()

 - Salve uma imagem do seu esquema em estrela:
  [Imagem do esquema]()

 - Escreva no readme o processo de construção do seu diagrama:
  Foi Criado a tabela Calendar seguindo a Dax mais abaixo. 
  para tabela produto uma agregação foi feita   

 - Fale sobre as etapas as funcionalidades e funções DAX utilizadas neste projeto:
  Para criação da tabela Calendar utilizei as seguintes funções DAX:
   - Calendar = CALENDARAUTO(12)
   - Day of the week = WEEKDAY('Calendar'[Date])
   - Day of the week 2 = FORMAT('Calendar'[Date], "DDDD")
   - Month Name = FORMAT(DATE(1,'Calendar'[Month Number],1), "MMM") 
   - Month Number = MONTH('Calendar'[Date])
   - Week Number = WEEKNUM('Calendar'[Date])
   - Year = YEAR('Calendar'[Date])

 [Financial Sample do Power BI]()