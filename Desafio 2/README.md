# Phyton | Desafios de projetos | Segundo desafio

## ✔Objetivo geral
Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário(cliente) e cadastrar conta bancária.

## 💥Desafio
Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar extrato. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário(cliente) e criar conta corrente(vincular com usuário)

### ⬇Função de depósito
A função depósito deve receber os argumentos apenas por posição (positional only). 

### ⬆Função de saque
A função de saque deve receber os argumentos apenas por nome (keyword only).

### 💱Função de extrato
A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). 
- Argumentos posicionais: saldo
- Argumentos nomeados: extrato

## 💢Novas funções
Precisamos criar duas novas funções: criar usuário e criar conta corrente.

### 👨Função criar usuário (cliente)
O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. 
O endereço é uma string com formato: logradouro, número da rua - bairro - cidade/sigla do estado.
Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF

### ♻Função criar conta corrente
O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário.
O número da conta é sequencial, iniciando em 1.
O número da agência é fixo: "0001".
O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

*** Obs.: Troquei usuário por cliente.