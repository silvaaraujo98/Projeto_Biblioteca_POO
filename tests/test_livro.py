from biblioteca.livro import Livro


livro_1 = Livro("Arte da Guerra","Sun Tzu","1234567",1990,5)


livro_1.adiciona_exemplares(2)
print(livro_1.emprestados)
