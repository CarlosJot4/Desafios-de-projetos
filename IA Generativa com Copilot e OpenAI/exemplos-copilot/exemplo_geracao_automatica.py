# exemplos-copilot/exemplo_geracao_automatica.py

def calcular_fibonacci(n):
    """
    Função gerada com GitHub Copilot.
    Retorna os n primeiros números da sequência de Fibonacci.
    """
    sequencia = [0, 1]
    while len(sequencia) < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia[:n]

if __name__ == "__main__":
    print(calcular_fibonacci(10))
