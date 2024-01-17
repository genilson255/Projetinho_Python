# Faça um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

nu = int(input("Informe um número: "))

dobro = nu * 2
triplo = nu * 3
raizQ = nu **(1/2)
raizC = nu ** (1/3)
print("O numero informado foi: {} o dobro dele é: {} "
      "o triplo dele é {} a raiz quadrada dele é: {} raiz Cubica {} "
      "".format(nu ,dobro, triplo, raizQ, raizC))

