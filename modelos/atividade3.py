#questão 1

#class Pessoa:
 #   def __init__(self, nome, idade, profissao):
  #      self.nome=nome
   #     self.idade=idade
    #    self.profisao=profissao

    #def __str__(self):
     #   return f'Nome: {self.nome} | Idade: {self.idade} | Profissã: {self.profisao}'
    

    #def aniversario (self):
     #  self.idade +=1

    #@property
    #def saudacao(self):
     #   if self.profisao == self.profisao:
      #      print(f'Olá {self.profisao} tenha um bom dia!')
       # else: print('tenha um pessimo dia')
        
#Pessoa1=Pessoa('Bernaro', '17', 'Vendedor')
#print(Pessoa1)

#questao 2 
class contabancaria:
    contas=[]
    def __init__(self,nome,saldo):
        self.nome=nome.title()
        self.saldo=saldo
        self._ativo=False
        contabancaria.contas.append(self)
#questao 3
    def __str__(self):
       # return self.nome
        return f'{self.nome}|{self.saldo}|{self.ativo}'

#questao 5 
    @classmethod
    def listar_restaurantes(cls):
        print(f'Nome do Titular | Saldo | Status')
        for conta in cls.contas:
            print(f'{conta.nome.ljust(20)}|{conta.saldo.ljust(20)}|{conta.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
#questao 4   
    def alternar_status(self):
        self._ativo=not self._ativo

conta1=contabancaria('Bernardo','100')
#questao 6
print(conta1.nome)

conta2=contabancaria('Murilo','60')

conta1.alternar_status()
conta2.alternar_status()

contabancaria.listar_restaurantes()

#questao 7
class ClienteBanco:
    def __init__(self, nome, sobrenome, idade, endereco, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone

    def __str__(self):
        return f'{self.nome}|{self.sobrenome}|{self.idade}|{self.endereco}|{self.telefone}'
    


#questão 8
cliente1=ClienteBanco('Bernardo','Batista',17,'Rua Joaquim Alfredo','(41)999999999')
cliente2=ClienteBanco('Maju','Lauxen',16,'Rua Joaquim Alvez Ferreira','(41)991952292')
cliente3=ClienteBanco('Murilo','Jossep',17,'Rua Arnaldo','(41)222222222')

print(cliente1)
print(cliente2)
print(cliente3)






