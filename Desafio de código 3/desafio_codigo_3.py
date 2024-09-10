class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

    def valor_total(self):
        return self.quantidade * self.valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        # TODOS: Verifique se o objeto passado é uma instância da classe Venda.
        # Isso ajuda a garantir que apenas vendas válidas sejam adicionadas ao relatório.
        if isinstance(venda, Venda):
            self.vendas.append(venda)
    
    def calcular_total_vendas(self):
        # Me retorna o valor total de todas as vendas na lsita de vendas
        return sum(venda.valor_total() for venda in self.vendas)


def main():
    relatorio = Relatorio()
    
    for _ in range(3):
        produto = input("Produto: ")
        quantidade = int(input("Quantidade: "))
        valor = float(input("Valor unitário: "))

        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)
    
    # TODOS: Exiba o total de vendas usando o método calcular_total_vendas.
    # Utilize o método `calcular_total_vendas` da classe `Relatorio` para mostrar o total acumulado das vendas.
    total_vendas = relatorio.calcular_total_vendas()
    print(f"Total de Vendas: {total_vendas:.2f}")


if __name__ == "__main__":
    main()