# Faça um Programa que leia um número inteiro
# e mostre na tela o seu sucessor e seu antecessor

n1 = int(input("Informe um numero: "))
sucess = n1 + 1
antec = n1 - 1
print("O numero informado foi {} seu antecessor é: {} seu sucesor é: {} ".format(n1, antec, sucess))
