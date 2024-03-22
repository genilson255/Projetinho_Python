n1 = int(input("Informe um valor: "))
n2 = int(input("Informe outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
ex = n1 ** n2

print("A soma é ({}),"
      "\n o produto é ({})"
      "\n e a divisão é {:.3f}"
      .format(s, m, d))
print('Divisao inteira ({}) e potencia {:.3f}  '
      '\n'.format(di, ex))
