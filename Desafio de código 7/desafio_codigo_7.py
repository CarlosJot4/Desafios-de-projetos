def filtrar_visuais(lista_visuais):
    # Converter a string de entrada em uma lista
    visuais = lista_visuais.split(", ")
    
    # TODO: Normalize e remova duplicatas usando um conjunto
    lista_normalizada = []

    for visual in visuais: # percorre cada elemnto da lsita
        visual = visual.title() # Normaliza os elementos da lista 
        lista_normalizada.append(visual)
    
    conjunto = set(lista_normalizada) #transforma a lista normalizada em um conjunto para remover elementos repetidos

    # TODO: Converta o conjunto de volta para uma lista ordenada:

    lista_final = list(conjunto)
    lista_final.sort()
    
    # Unir a lista em uma string, separada por vírgulas
    return ", ".join(lista_final)

# Capturar a entrada do usuário
entrada_usuario = input()

# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)