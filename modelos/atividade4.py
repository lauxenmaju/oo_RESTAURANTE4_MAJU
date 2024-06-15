#questão1

class livro:
    livros=[]
    livros_disponiveis=[]
    def __init__(self,titulo,autor,ano_publicacao,disponibilidade):
        self.titulo=titulo
        self.autor=autor
        self.ano_publicacao=ano_publicacao
        self._disponivel=True
        self.disponibilidade=disponibilidade
        livro.livros.append(self)

        if self.disponibilidade == 'Disponível':
            livro.livros_disponiveis.append(self)
#questão 4
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis_no_ano = []
        for livros in livro.livros_disponiveis:
            if livro.ano_publicacao == ano:
                livros_disponiveis_no_ano.append(livro)
        return livros_disponiveis_no_ano
#questao2
    def __str__(self):
       # return self.nome
        return f'{self.titulo}|{self.autor}|{self.ano_publicacao}|{self._disponivel} '
    
    @classmethod
    def listar_livros(cls):
        print(f'Título | Autor | Ano de publicação | Status')
        for livro in cls.livros:
            print(f'{livro.titulo.ljust(20)}|{livro.autor.ljust(20)}| {str(livro.ano_publicacao).ljust(20)} | {livro._disponivel}')
#questao3
    def emprestar(self):
        self._disponivel=not self._disponivel
        print('Homem aranha está disponível | Os sete maridos de evelyn hugo não está disponível')


#questão2   
#livro1=livro('Homem aranha','Tom','2021','Disponìvel')
#livro2=livro('Os sete maridos de evelyn hugo','Jenny','2019','Emprestado')

#questão 4
ano_desejado = 2019
livros_disponiveis_2019= livro.verificar_disponibilidade(ano_desejado)

print(f'Livros disponíveis em {ano_desejado}:')
for livro in livros_disponiveis_2019:
    print(f'{livro.titulo} ({livro.autor})')
#questão3
#livro1.emprestar()

livro.listar_livros()


