# Faça um algoritimo que leia o salário de um funcionário e mostrese novo
# salario, com almento de 15%

acrescimo = 0.15
preco: float = float(input('Valor do produto: '))
newSalary = preco + (preco * acrescimo)
print('O salário infromado foi: {} novo salário com o acrescimo fica: {}'.format(preco, newSalary, preco))

