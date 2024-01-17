# Faça um algoritimo que leia um numero e mostre o seu dobro,
# triplo e raiz quadrada

nu = int(input("Informe um número: "))

dobro = nu * 2
triplo = nu * 3
raizQ = nu **(1/2)
raizC = nu ** (1/3)
print("O numero informado foi: {} \n o dobro dele é: {} \n"
      "o triplo dele é {:.3f} \n a raiz quadrada dele é: {:.3f} \n raiz Cubica {:.3} "
      "".format(nu ,dobro, triplo, raizQ, raizC))

