import random

# Escolher 2 números primos para iniciar a criptografia
p = 7
q = 11
n = p * q

# 50 Possibilidades de valores para E
possib = list()
a = 0
m = 2
while a != 50:
    if m % p != 0 and m % q != 0 and m % n != 0:
        possib.append(m)
        a += 1
    m += 1

# E escolhido aleatoriamente entre 50 possibilidades
e = random.choice(possib)

print(e)


# OUU

# e = menor numero coprimo de n que nao seja par e 1 (menor possivel = 3)

m = 3
e = 0
while e == 0:
    if m % p1 != 0 and m % p2 != 0 and m % n != 0:
        e = m;
    m += 1

##################


# d = inv_mult(e,phi)


def coprimos(phi):
    coprimos = []
    sao = False
    for div in range(1, phi):
        for i in range (2,div):
            if div % i == 0 and phi % i == 0:
                sao = False
        if sao == True:
            coprimos.append(div)
        sao = False
    return coprimos