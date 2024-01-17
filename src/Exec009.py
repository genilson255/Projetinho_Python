# Faça um algoritimo que leia o preço de um produto,
# e mostre seu novo preço, com 5% de desconto

desconto = 0.05
preco: float = float(input('Valor do produto: '))
produto = preco - (preco * desconto)
print('O preço infromado foi: {} produto com desconto fica: {}'.format(preco, produto, preco))
