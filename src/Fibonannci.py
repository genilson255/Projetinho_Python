# Fibonacci é uma sequência de números, que aparece em
# certos mistérios da natureza e da vida, onde a sequência
# inicia com 0 e 1, e os números seguintes serão a soma dos
# dois números anterior.
#
# Por exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

ante = 0
prox = 0
while( prox < 10):
    print(prox)
    prox = prox + ante
    ante = prox - ante
    if(prox == 0):
        prox += 1