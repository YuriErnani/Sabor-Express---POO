from Modelos.restaurante import Restaurante
from Modelos.Cardapio.bebida import Bebida
from Modelos.Cardapio.prato import Prato

restaurante1 = Restaurante('Fogo Gaúcho Grill', 'Churrascaria Brasileira')
bebida_suco = Bebida('Suco de Laranja', 5.0, 'Grande')
bebida_suco.aplicar_desconto()

prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()

restaurante1.adicionar_no_cardapio(bebida_suco)
restaurante1.adicionar_no_cardapio(prato_paozinho)

def exibir_nome_do_programa():

    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n''')

def main():
    exibir_nome_do_programa()
    restaurante1.exibir_cardapio

if __name__ == '__main__':
    main()