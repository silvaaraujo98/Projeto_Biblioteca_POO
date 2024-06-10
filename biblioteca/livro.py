class Livro():
    def __init__(self, titulo,autor,isbn, ano_publicacao,numero_exemplares):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao
        self.numero_exemplares = numero_exemplares
        self.emprestados = 0

    def adiciona_exemplares(self,n_exemplares_adicionados):
        self.numero_exemplares += n_exemplares_adicionados
    
    def remover_exemplares(self,n_exemplares_removidos):
        self.numero_exemplares -= n_exemplares_removidos


    def emprestar_exemplar(self):
        if self.emprestados == self.numero_exemplares:
            print("Não há exemplares disponíveis")
        else:
            self.emprestados +=1
    
    def devolver_exemplar(self):
        self.emprestados -=1 
        print("Obrigado por Devolver o Livro")
