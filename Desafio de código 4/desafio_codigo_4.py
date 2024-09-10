class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

    def valor_total(self):
        return self.quantidade * self.valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    # TODOS: Implementar o método adicionar_venda para adicionar uma venda à lista de vendas:
    def adicionar_venda(self, venda):
    # Adiciona uma venda a lista de vendas, se for uma instância válida da classe Venda.
        if isinstance(venda, Venda):
            self.vendas.append(venda)
    # TODOS: Implementar o método total_vendas para calcular e retornar o total das vendas
    def total_vendas(self):
    # Calcula o total de todas as vendas da lista de vendas SEM CONSIDERAR A QUANTIDADE
        return sum(venda.valor for venda in self.vendas)


def main():
    categorias = []

    for _ in range(2):
        nome_categoria = input("Nome da categoria: ")
        categoria = Categoria(nome_categoria)

        for _ in range(2): 
            entrada_venda = input("Digite o produto, quantidade e o valor (ex: Produto, 4, 4.99)")
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())

            venda = Venda(produto.strip(), quantidade, valor)
            # TODOS: Adicione a venda à categoria usando o método adicionar_venda:
            categoria.adicionar_venda(venda)

        categorias.append(categoria)
    
    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
      # TODOS: Exibir o total de vendas usando o método total_vendas:
      total_vendas = categoria.total_vendas()
      print(f"Vendas em {categoria.nome}: {total_vendas:.2f}")

if __name__ == "__main__":
    main()