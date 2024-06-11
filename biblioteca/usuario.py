class Usuario():
    def __init__(self,nome,cpf,email,telefone,endereco,livros_emprestados = []):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__endereco = endereco
        self.livros_emprestados = livros_emprestados

    def set_atualiza_informacoes(self,nome=False,cpf = False,email = False,telefone = False,endereco = False):
        if not nome:
            self.__nome = nome
        elif not cpf:
            self.__cpf = cpf
        elif not email:
            self.__email = email
        elif not telefone:
            self.__telefone = telefone
        elif not endereco:
            self.__endereco = endereco

    def adiciona_livro_emprestado(self,Livro):
        self.livros_emprestados.append(Livro)
        Livro.emprestar_exemplar()
    
    def devolve_livro_emprestado(self,Livro):
        if Livro in self.livros_emprestados:
            self.livros_emprestados.remove(Livro)
            Livro.devolver_exemplar()
        
        else:
            print("Você não tem esse livro na sua lista de livros emprestados")

    def get_informacoes_gerais_usuarios(self):
        print(f"O usuario de nome {self.__nome} possui {len(self.livros_emprestados)} emprestados")
