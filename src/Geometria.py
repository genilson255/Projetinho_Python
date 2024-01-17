# A fórmula é conforme abaixo, onde é apresentada o teorema de
# Pitágoras que faz a afirmação para todo triângulo retângulo,
# a soma dos quadrados dos catetos é igual ao quadrado da hipotenusa:
# a² = b² + c²


catetoOposto = float(input('Entre com o valor do cateto oposto: '))
catetoAdjacente = float(input('Entre com o valor do cateto adjacente: '))
hipotenusa = (catetoAdjacente ** 2 + catetoOposto ** 2) ** (1/2)
print('**********************************************')
print('O valor da hipotenusa é: {}'.format(hipotenusa))
print('===============================================')
