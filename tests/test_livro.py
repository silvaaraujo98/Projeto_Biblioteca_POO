from biblioteca.livro import Livro


livro_1 = Livro("Arte da Guerra","Sun Tzu","1234567",1990,5)


livro_1.adiciona_exemplares(2)
print(livro_1.emprestados)

print(livro_1.numero_exemplares)

livro_1.emprestar_exemplar()
print(livro_1.emprestados)
livro_1.emprestar_exemplar()
print(livro_1.emprestados)
livro_1.emprestar_exemplar()
print(livro_1.emprestados)
livro_1.emprestar_exemplar()
print(livro_1.emprestados)
livro_1.emprestar_exemplar()
print(livro_1.emprestados)
livro_1.emprestar_exemplar()
print(livro_1.emprestados)
livro_1.emprestar_exemplar()

livro_1.get_informacoes_gerais()
