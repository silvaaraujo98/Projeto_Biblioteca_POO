from biblioteca.livro import Livro
from biblioteca.usuario import Usuario
from biblioteca.emprestimo import Emprestimo
import datetime

livro_1 = Livro("Arte da Guerra","Sun Tzu","1234567",1990,5)
livro_2 = Livro("Meditações","Marco Aurelio","88888888",2023,3)

usuario_1 = Usuario("João da Silva",11111111111,"jvsilvaaraujo98@gmail.com",99999999,"Rua 25")
usuario_2 = Usuario("Carla Vieira",22222222,"carla.vieira@gmail.com",19999999,"Rua 88")

emprestimo_1 = Emprestimo(usuario_1,livro_1,datetime.datetime(2024,11,6))
emprestimo_1.registrar_emprestimo()


emprestimo_2 = Emprestimo(usuario_2,livro_1,datetime.datetime(2024,11,6))
emprestimo_2.registrar_emprestimo()
emprestimo_2.usuario.get_informacoes_gerais_usuarios()