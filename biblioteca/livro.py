class Livro():
    def __init__(self, titulo,autor,isbn, ano_publicacao,numero_exemplares):
        self.__titulo = titulo #AtributoPrivado
        self.__autor = autor #AtributoPrivado
        self.isbn = isbn 
        self.__ano_publicacao = ano_publicacao #AtributoPrivado
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


    @property
    def get_title(self):
        return self.__titulo
    
    
    def get_informacoes_gerais(self):
        print( f"O livro de titulo {self.__titulo} de autor {self.__autor} e isbn {self.isbn} com ano de publicação em {self.__ano_publicacao}")
        print(f"Possui {self.numero_exemplares} número de exemplares sendo que destes  {self.emprestados} estão emprestados")

