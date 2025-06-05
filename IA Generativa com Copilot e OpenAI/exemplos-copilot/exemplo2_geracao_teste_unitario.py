# exemplos-copilot/exemplo2_geracao_teste_unitario.py

def eh_palindromo(texto):
    """
    Verifica se o texto é um palíndromo (palavra que se pode ler da esquerda para a direita ou vice-versa, sem mudanças.).
    Ignora espaços e diferenciação entre maiúsculas/minúsculas.
    """
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

# Teste unitário gerado automaticamente com Copilot
import unittest

class TestPalindromo(unittest.TestCase):
    def test_palindromo_simples(self):
        self.assertTrue(eh_palindromo("arara"))

    def test_com_espacos(self):
        self.assertTrue(eh_palindromo("A sacada da casa"))

    def test_nao_palindromo(self):
        self.assertFalse(eh_palindromo("Python"))

if __name__ == '__main__':
    unittest.main()
