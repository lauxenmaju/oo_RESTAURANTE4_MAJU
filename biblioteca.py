#questão 5
from modelos.atividade4 import livro

livro1=livro('Homem aranha','Tom','2021','Disponível')
livro2=livro('Os sete maridos de evelyn hugo','Jenny','2019','Emprestado')

#questão 6
livro1.emprestar()

#questão 7
def main():
    livro.listar_livros()

if __name__ =='__main__':
    main()