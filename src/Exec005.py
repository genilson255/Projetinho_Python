# Escreva um programa que leia um valor em metros e o exiba
# convertido em centimetros e milimetros

nu = float(input("Informe a medida para ser convertido: "))
km = nu * 1000 # mil metros
hm = nu * 100 # metros
dam = nu * 10
m = nu * 100
dm = nu * 10
cm = nu * 100 #cm
mm = nu * 1000 #mm
dc = nu * 10
print(''
      'O valor informado foi: {}mt'
      '\n convertido em km {}km'
      '\n convertido em hm {}hm'
      '\n convertido em dam: {}dam'
      '\n convertido em metro: {}m '
      '\n convertido em dm: {}dm '
      '\n convertido em centimetro: {}cm '
      '\n convertido em milimetro: {}mm '
      '\n convertido em decimetro: {}dc '
      '\n'.format(nu, km, hm, dam, m, dm, cm, mm, dc))

