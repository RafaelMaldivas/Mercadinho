from typing import List, Dict
from time import sleep
from model.produtos import Produto
from emoji import emojize

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()


def menu() -> None:
    print(emojize(':leaves::leaves::leaves::leaves::leaves::leaves::leaves::leaves::leaves::leaves:', use_aliases=True ))
    print('=========== Bem Vindo ===============')
    print(emojize('=======:mushroom: SMOKE WEED AND HEALTH:herb: =======', use_aliases=True))
    print(emojize(':leaves::leaves::leaves::leaves::leaves::leaves::leaves::leaves::leaves::leaves:', use_aliases=True ))

    print(emojize(':arrow_down: Selecione uma opção abaixo :arrow_down:', use_aliases=True))
    print(emojize(':arrow_forward: [1] Cadastrar Produtos'))
    print(emojize(':arrow_forward: [2] Listar Produtos'))
    print(emojize(':arrow_forward: [3] Comprar Produtos'))
    print(emojize(':arrow_forward: [4] Visualizar Carrinho'))
    print(emojize(':arrow_forward: [5] Fechar Pedido'))
    print(emojize(':arrow_forward: [6] Sair do Sistema'))

    opcao: int = int(input(emojize("Digite a opção desejada :soon:", use_aliases=True)))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produto()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print(emojize('Volte Sempre :wave:', use_aliases=True))
        sleep(2)
        exit(0)
    else:
        print(emojize(':-1: Opção Inválida!  :speech_balloon:', use_aliases=True))

def cadastrar_produto() -> None:
    print('================================')
    sleep(0.5)
    print(emojize('====== :gift: Cadastro de Produtos :gift: ======', use_aliases=True))
    sleep(0.5)
    print('===================================')
    sleep(0.5)
    nome: str = input('Digite o nome do produto : ')
    preco: float = float(input('Digite o preço do produto : '))
    qnt: int = int(input('Digite a quantidade do produto'))



def listar_produto() -> None:
    pass


def comprar_produto() -> None:
    pass


def visualizar_carrinho() -> None:
    pass


def fechar_pedido() -> None:
    pass

def id_produto(cod:int) -> Produto:
    pass


if __name__ == '__main__':
    main()


