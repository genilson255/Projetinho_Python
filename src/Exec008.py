# Faça um programa que leia a largura de uma parede em metros, e
# calcule a sua area e a quantidade de
# tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta um área de 2m²

largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))
litroTinta = 2 ** 2

areaParede = largura * altura
paredePintada = areaParede / litroTinta
print('O tamanho da parede é de: {} total de tinta para pintá-la: {} litros de tinta'.format(areaParede, paredePintada))

