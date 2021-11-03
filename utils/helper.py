def formata_float_str_moeda(valor: float) -> str:
    return f' R$ {valor:,.2f} '

def formata_qtd_gramas(valor: int) -> str:
    return f'{valor} gr'

def formata_qtd_ml(valor: int) -> str:
    return f'{valor} mL'
