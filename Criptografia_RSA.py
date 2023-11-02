# Funções/Bibliotecas/Tuplas
import random
from time import sleep

concluido = "\n¬ Concluído! Voltando ao menu..."


def menu():
    print("\n\033[1m" + "==============\033[47;1;30m MENU \033[0;0m==============" + "\033[m")
    print("\033[33m(1)\033[m - Gerar chaves aleatoriamente")
    print("\033[32m(2)\033[m - Gerar chaves manualmente")
    print("\033[36m(3)\033[m - Criptografar uma mensagem")
    print("\033[35m(4)\033[m - Decriptografar uma mensagem")
    print("\033[31m(5)\033[m - Sair")
    print("=" * 35)
    op = input("> Digite a opção desejada: ")
    while op not in '12345':  # Validação
        op = input("! Digite uma das opções do menu: ")
    return op


def primos(limite):
    primo = True
    primos = []
    for i in range(3, limite):
        for j in range(2, i):
            if i % (j) == 0:
                primo = False
        if primo:
            primos.append(i)
        primo = True
    return primos

def verifprimos(n):
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
    return primo


def mdc(a, b):
    if b == 0:
        return a
    resto = a % b
    a = b
    b = resto
    return mdc(a, b)


def coprimos(n):
    coprimos = []
    for i in range(3, n):
        if mdc(i, n) == 1:
            coprimos.append(i)
    return coprimos


def valid_n(n):
    divisores_n = list()
    for i in range(2, n):
        if n % i == 0:
            divisores_n.append(i)
        if len(divisores_n) == 2:
            valido = True
        else:
            valido = False
    return valido


# Apresentação/Menu
op = menu()

while op in '1234':
    print("\n\n" + "-" * 35)
    if op == '1':
        print("\033[33m(1)\033[m - Gerar chaves aleatoriamente")

        # Definindo n
        p1, p2 = random.choice(primos(100)), random.choice(primos(100))
        while p1 == p2:
            p1, p2 = random.choice(primos(100)), random.choice(primos(100))
        n = p1 * p2

        # Definindo e
        phi_n = (p1 - 1) * (p2 - 1)
        e = random.choice(coprimos(phi_n))

        # Definindo d
        d = 0
        i = 1
        while d == 0:
            if (i * e) % phi_n == 1:
                d = i
            i += 1

        print(f"\033[33m#\033[m Chaves \033[1mPúblicas\033[m: e = {e}, p1 = {p1}, p2 = {p2}")
        print(f"\033[33m#\033[m Chaves \033[1mPrivadas\033[m: d = {d}, n = {n}")

    if op == '2':
        print("\033[32m(2)\033[m - Gerar chaves manualmente")

        # Definindo p1, p2, n e phi(n)
        p1 = int(input("\033[32m>\033[m Digite o primeiro número primo: "))
        while not verifprimos(p1):
            p1 = int(input("\033[32m!\033[m O número digitado não é primo. Tente outro: "))

        p2 = int(input("\033[32m>\033[m Digite o segundo número primo: "))
        while p2 == p1 or not verifprimos(p2):
            if p2 == p1:
                p2 = int(input("\033[32m!\033[m Os números devem ser diferentes. Tente outro: "))
            if not verifprimos(p2):
                p2 = int(input("\033[32m!\033[m O número digitado não é primo. Tente outro: "))

        n = p1 * p2
        phi_n = (p1 - 1) * (p2 - 1)
        print(f"* phi(n) = {phi_n}\n")

        # Definindo e
        e = int(input("\033[32m>\033[m Digite um número coprimo de phi(n) e menor que ele: "))
        while e not in coprimos(phi_n):
            print("\033[32m!\033[m Número inválido. As possibilidades são: ", coprimos(phi_n))
            e = int(input("\033[32m>\033[m Digite um número coprimo de phi(n) e menor que ele: "))

        # Definindo d
        d = 0
        i = 1
        while d == 0:
            if (i * e) % phi_n == 1:
                d = i
            i += 1

        print(f"\033[32m#\033[m Chaves \033[1mPúblicas\033[m: e = {e}, p1 = {p1}, p2 = {p2}")
        print(f"\033[32m#\033[m Chaves \033[1mPrivadas\033[m: d = {d}, n = {n}")

    if op == '3':
        print("\033[36m(3)\033[m - Criptografar uma mensagem")

        # Recebendo e validando a mensagem a ser criptografada
        msg = input("\033[36m>\033[m Digite a mensagem a ser criptografada: ")
        while len(msg) > 128:
            msg = input("\033[36m!\033[m A mensagem não deve exceder 128 caracteres, tente outra: ")

        # Recebendo e validando as chaves
        p1 = int(input("\033[36m>\033[m Digite a chave p1: "))
        while not verifprimos(p1):
            p1 = int(input("\033[36m!\033[m Chave inválida. Tente outra: "))

        p2 = int(input("\033[36m>\033[m Digite a chave p2: "))
        while p1 == p2:
            p2 = int(input("\033[36m!\033[m As chaves devem ser diferentes. Tente outra: "))
        while not verifprimos(p2):
            p2 = int(input("\033[36m!\033[m Chave inválida. Tente outra: "))

        phi_n = (p1 - 1) * (p2 - 1)
        e = int(input("\033[36m>\033[m Digite a chave e: "))
        while e not in coprimos(phi_n):
            e = int(input("\033[36m!\033[m Chave inválida. Tente outra: "))

        # Transformando o texto em números (ASCCI)
        msg_ascci = []
        for i in range(0, len(msg)):
            msg_ascci.append(ord(msg[i]))

        # Criptografando: C = M^e mod n
        n = p1 * p2
        crip = []
        for i in range(0, len(msg)):
            crip.append((msg_ascci[i] ** e) % n)

        # Apresentando a mensagem criptografada
        print("\033[36m#\033[m Mensagem criptografada: ", end="")
        for i in range(0, len(crip)):
            print(crip[i], "", end="")
        print("\n")

    if op == '4':
        print("\033[35m(4)\033[m - Decriptografar uma mensagem")

        # Recebendo a mensagem a ser decriptografada em uma lista
        crip = input("\033[35m>\033[m Digite a mensagem a ser decriptografada: ").split()
        for i in range(0, len(crip)):
            crip[i] = int(crip[i])

        # Recebendo as chaves
        d = int(input("\033[35m>\033[m Digite a chave d: "))
        n = int(input("\033[35m>\033[m Digite a chave n: "))

        # Decriptografando: M = C^d mod n
        dascci = []
        for i in range(0, len(crip)):
            dascci.append(chr(((crip[i] ** d) % n)))

        # Apresentando a mensagem decriptografada
        print("\033[35m#\033[m Mensagem decriptografada: ", end="")
        for i in range(0, len(crip)):
            print(dascci[i], end="")
        print("\n")

    # Mensagem de operação concluída e reapresentãção do menu
    for i in concluido:
        print(i, end='')
        sleep(0.1)
    print("\n" + "-" * 35 + "\n\n")
    op = menu()

# Finalização
print("\n\n\033[31m(5)\033[m - Sair")
print("\033[31m#\033[m Finalizado. Obrigada!")
