from model.produtos import Produto

nome = 'Prensado'
preco = 100
qtd = 25
desc ='quantidade vendida em gramas'

pren = Produto(nome, preco, qtd, desc)
gold = Produto('Colombia Gold', 100, 5,"qunatidade vendida em gramas")
print(pren)
print(gold)