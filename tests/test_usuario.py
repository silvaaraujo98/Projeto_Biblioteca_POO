from biblioteca.livro import Livro
from biblioteca.usuario import Usuario


livro_1 = Livro("Arte da Guerra","Sun Tzu","1234567",1990,5)
livro_2 = Livro("Meditações","Marco Aurelio","88888888",2023,3)

usuario_1 = Usuario("João da Silva",11111111111,"jvsilvaaraujo98@gmail.com",99999999,"Rua 25")


usuario_1.adiciona_livro_emprestado(livro_1)

