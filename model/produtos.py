from utils.helper import formata_float_str_moeda

class Produto:

    contador: int = 1

    def __init__(self: object, nome:str, preco:float, qtd:int, desc:str) -> None:
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self.__preco : float = preco
        self.__quantidade: int = qtd
        self.__descricao: str = desc
        Produto.contador += 1

    @property
    def codigo(self:object) -> int:
        return self.__codigo

    @property
    def nome(self:object)-> str:
        return self.__nome

    @property
    def preco(self:object) -> float:
        return self.__preco

    @property
    def quantidade(self:object) -> int:
        return  self.__quantidade

    @property
    def descricao(self:object) -> str:
        return self.__descricao

    def calcula_total(self:object, qtd:int , preco:float) -> str:
        return  f'Valor Total: R$ {qtd * preco} '


    def __str__(self) -> str:
        return f'-----------------------------------------------------------------------------\n' \
               f'Código : {self.codigo} \nNome : {self.nome}\n' \
               f'Preço: {formata_float_str_moeda(self.preco)}\nQuantidade : {self.quantidade}' \
               f'\nDescrição: {self.descricao}\n{self.calcula_total(self.quantidade, self.preco)}'
