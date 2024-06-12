class Biblioteca ():
    def __init__(self,nome_biblioteca,lista_livros=[],lista_usuarios = [],lista_emprestimos = []):
        self.nome_biblioteca = nome_biblioteca
        self.livros = lista_livros
        self.usuarios = lista_usuarios
        self.emprestimos = []

    def adicionar_livros(self,livro):
        for livro_existente in self.lista_livros:
            if livro.isbn == livro_existente.isbn:
                print("Livro já está no Banco de Dados")
            else:
                self.livros.append(livro)

    
    def remove_livro(self,livro):
        for livro_existente in self.livros:
            if livro.isbn == livro_existente.isbn:
                self.livros.remove(livro)
                print("Livro Removido com Suceso")
                break
        else:
                print("O Livro Buscado não está na Base de Dados para ser Removido")

    def buscar_livro(self,livro):
        for livro_existente in self.livros:
            if livro.isbn == livro_existente.isbn:
                livro_existente.get_informacoes_gerais()
                break
        else:
                print("A Biblioteca não possui o livro buscado")

    def adicionar_usuario(self,usuario):
        for usuario_existente in self.usuarios:
            if usuario_existente.get-cpf() == usuario.get_cpf():
                print("O Usuario com esse cpf ja ta cadastrado na Biblioteca")
                break
        else:
            self.usuarios.append(usuario)
            print("Usuario Cadastrado com Sucesso")


    def remover_usuario(self,usuario):
        for usuario_existente in self.usuarios:
            if usuario_existente.get_cpf() == usuario.get_cpf():
                self.usuarios.remove(usuario)
                print("O Usuario Removido com Sucesso")
                break
        else:
            print("O Usuario não esta no nosso banco de dados")

    
            