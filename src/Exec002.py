# Faça um Programa que leia um número inteiro
# e mostre na tela o seu sucessor e seu antecessor

'''n1 = int(input("Informe um numero: "))
sucess = n1 + 1
antec = n1 - 1
print("O numero informado foi {} seu antecessor é: {} seu sucesor é: {} ".format(n1, antec, sucess))
'''

# Para i na lista 234, 654, 378, 798:
'''for i in [234, 654, 378, 798]:
 # Se o resto dividindo por 3 for igual a zero:
    if i % 3 == 0:
        print(i, '/ 3 =', i / 3)'''

s = 0
for x in range(1, 100):
    s = s + x
    print( s)
