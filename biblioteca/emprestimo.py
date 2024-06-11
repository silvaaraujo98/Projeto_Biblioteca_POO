class Emprestimo():
    def __init__(self,usuario,livro,data_emprestimo):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None
        


    def registrar_emprestimo(self):
        self.usuario.adiciona_livro_emprestado(self.livro)
    
    
    def registrar_devolucao(self,data_devolucao):
        self.usuario.devolve_livro_emprestado(self.livro)
        self.data_devolucao = data_devolucao

    def verificar_status(self):
        if self.data_devolucao is None:
            print("O livro nao foi devolvido ainda")
        else:
            print(f"O livro foi devolvido na data {self.data_devolucao}")