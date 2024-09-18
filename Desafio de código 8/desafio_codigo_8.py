def extrair_anos(datas):
    # Divide a string de datas em uma lista
    lista_datas = datas.split(", ")
    # TODO: Extraia o ano de cada data e cria uma nova lista com os anos
    
    anos = []
    for data in lista_datas: # percorre cada elemnto da lista de datas
        anos.append(data[:4]) # pega os 4 primeiros digitos da data que é o ano

    # Junta os anos em uma string separada por vírgula e retorna
    return ", ".join(anos)


entrada = input()

# TODO: Chame a função para imprimir o resultado:
saida = extrair_anos(entrada)
print(saida)