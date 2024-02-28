from Modelos.restaurante import Restaurante

restaurante1 = Restaurante('Fogo Gaúcho Grill', 'Churrascaria Brasileira')

restaurante1.receber_avaliacao('Yuri', 10)
restaurante1.receber_avaliacao('Ana', 7)
restaurante1.receber_avaliacao('Eduardo', 8)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()