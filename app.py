#criando versão padrão de mercado

from modelos.restaurante4 import Restaurante

restaurante1=Restaurante('salgadinho sabor chule', 'petiscos')
restaurante2=Restaurante('Saco do feijão', 'feijoada')
restaurante3=Restaurante('Calabreso', 'massas')

restaurante3.alternar_status()
restaurante3.receber_avaliacao('Ronaldo',4)
restaurante3.receber_avaliacao('Amanda',3)

def main():
    Restaurante.listar_restaurantes()

if __name__ =='__main__':
    main()