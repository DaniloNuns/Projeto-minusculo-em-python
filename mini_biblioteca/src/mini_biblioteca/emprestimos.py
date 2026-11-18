from .livros import Livro
from .usuarios import Usuario

class Emprestimo:
    def __init__(self, livro, usuario, ativo):
        self.livro = Livro
        self.Usuario = Usuario
        self.ativo = True
        self.disponivel = False

    if self.livro.disponivel == False:
        raise ValueError("Não pode emprestar um livro que ja está indisponível.")

