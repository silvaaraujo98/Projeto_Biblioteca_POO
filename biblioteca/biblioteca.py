class Biblioteca ():
    def __init__(self,nome_biblioteca,lista_livros=[],lista_usuarios = [],lista_emprestimos = []):
        self.nome_biblioteca = nome_biblioteca
        self.livros = lista_livros
        self.usuarios = lista_usuarios
        self.emprestimos = []

    def adicionar_livros(self,livro):
        for livro_existente in self.lista_livros:
            if vars(livro) == vars(livro_existente):
                print("Livro já está no Banco de Dados")
            else:
                self.livros.append(livro)

    
    def remove_livro(self,livro):
        for livro_existente in self.livros:
            if vars(livro) == vars(livro_existente):
                self.livros.remove(livro)
                print("Livro Removido com Suceso")
                break
        else:
                print("O Livro Buscado não está na Base de Dados para ser Removido")

    def buscar_livro(self,livro):
        for livro_existente in self.livros:
            if vars(livro) == vars(livro_existente):
                livro_existente.get_informacoes_gerais()
                break
        else:
                print("A Biblioteca não possui o livro buscado")

    def adicionar_usuario(self,usuario):
        for usuario_existente in self.usuarios:
            if vars(usuario_existente) == vars(usuario):
                print("O Usuario com esse cpf ja ta cadastrado na Biblioteca")
                break
        else:
            self.usuarios.append(usuario)
            print("Usuario Cadastrado com Sucesso")


    def remover_usuario(self,usuario):
        for usuario_existente in self.usuarios:
            if vars(usuario_existente) == vars(usuario):
                self.usuarios.remove(usuario)
                print("O Usuario Removido com Sucesso")
                break
        else:
            print("O Usuario não esta no nosso banco de dados")

    def buscar_usuario(self,usuario):
        for usuario_existente in self.usuarios:
            if vars(usuario_existente)== vars(usuario):
                usuario_existente.get_informacoes_gerais_usuarios()
                break
        else:
            print("O Usuario não esta no nosso banco de dados")

    def registra_emprestimo(self,emprestimo):
        for emprestimo_existente in self.emprestimos:
            if vars(emprestimo_existente) == vars(emprestimo):
                print("Já há um empréstimo com essas características na Base de Dados")
        else:
             self.emprestimos.append(emprestimo)


    def registra_devolucao(self,emprestimo):
        for emprestimo_existente in self.emprestimos:
            if vars(emprestimo_existente) == vars(emprestimo):
                self.emprestimos.remove(emprestimo)
                
        else:
             print("Não há um empréstimo com essas características na Base de Dados")

    def gera_relatorio_livros_disponiveis(self):
        for livro in self.livros:
            if livro.numero_exemplares == livro.emprestados:
                pass
            else:
                livro.get_informacoes_gerais()


    def gera_relatorio_livros_emprestados(self):
        for livro in self.livros:
            if livro.emprestados != 0:
                disponiveis = livro.numero_exemplares - livro.emprestados
                print(f"O livro {livro.get_title} possui {livro.emprestados} exemplares emprestados e {disponiveis} exemplares disponiveis")
            else:
                pass


    def gera_relatorio_de_usuarios_com_emprestimos(self):
        for usuario in self.usuarios:
            if usuario.livros_emprestados != []:
                lista_livros_emprestados = [livro.get_title for livro in usuario.livros_emprestados]
                usuario.get_informacoes_gerais_usuarios()
                print(f"E os livros emprestados são os seguintes:{lista_livros_emprestados}")


    
            