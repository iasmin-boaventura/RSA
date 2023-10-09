# Funções/Bibliotecas/Tuplas/Classes
import random


def primos(limite):
    primo = True
    primos = []
    for i in range(3, limite):
        for j in range(2, i):
            if i % (j) == 0:
                primo = False
        if primo == True:
            primos.append(i)
        primo = True
    return primos


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


# Apresentação/Menu
print("\n\033[1m"+"===== CRIPTOGRAFIA RSA ====="+"\033[m")
print("\033[36m"+"(C) - CRIPTOGRAFAR"+"\033[m")
print("\033[35m"+"(D) - DECRIPTOGRAFAR"+"\033[m")
print("="*28)
op = input("> Digite a opção desejada: ").upper()

while op not in 'CD':  # Validação
    op = input("! Digite (C) para Criptografar ou (D) para Decriptografar: ").upper()

print("="*28)
while op in 'CD':
    if op == 'C':  # CRIPTOGRAFAR
        print("\n\033[36m" + "(C) - CRIPTOGRAFAR" + "\033[m")
        print("\nPara criptografar pelo método RSA, definiremos as \033[1mchaves públicas (e, n)\033[m e \033["
              "1mprivadas (d, n)\033[m:")
        input()
        # Definindo n
        print("\n1) A chave \033[33m(n)\033[m é definida pela multiplicação de dois números primos.\n"
              "*** Aqui são escolhidos dois primos aleatórios no intervalo de 3 a 50, para simples demonstração.")

        p1, p2 = random.choice(primos(50)), random.choice(primos(50))
        while p1 == p2:
            p1, p2 = random.choice(primos(50)), random.choice(primos(50))
        n = p1 * p2

        print(f"\nPrimo 1: {p1}\nPrimo 2: {p2}")
        print(f"n = p1 * p2 = {p1} * {p2} = {n}")
        input()

        # Definindo e
        print("\n2) A chave \033[33m(e)\033[m obedece as condições: 1 < e < phi(n) e coprimo de phi(n)\n")
        phi_n = (p1 - 1) * (p2 - 1)
        e = random.choice(coprimos(phi_n))
        print(f"\nphi(n) = (p1 - 1) * (p2 - 1) = ({p1} - 1) * ({p2} - 1) = {phi_n}\n"
              f"e = {e} (maior que 1, menor que phi(n) e coprimo de phi(n)\n")
        input()

        # Definindo d
        print(
            "\n3) A chave privada \033[33m(d)\033[m é o inverso modular da chave pública (e), obedecendo a condição: "
            "(d * e) mod phi_n = "
            "1\n ")
        d = 0
        i = 1
        while d == 0:
            if (i * e) % phi_n == 1:
                d = i
            i += 1

        print(f"d = {d}\n")
        input()

        print(f"\033[32m||| Chaves Públicas: e = {e}, n = {n}")
        print(f"||| Chaves Privadas: d = {d}, n = {n}\033[m\n")

        msg = input("\nAgora, digite a mensagem a ser criptografada: ")

        # Transformando o texto em números (ASCCI)
        msg_ascci = []
        for i in range(0, len(msg)):
            msg_ascci.append(ord(msg[i]))
        print(f"\nCada caractere é transformado ao seu equivalente decimal em ASCCI:\n"
              f"> Mensagem em caractere: {msg}\n"
              f"> Mensagem em decimal: ", end="")
        for i in range(0, len(msg_ascci)):
            print(msg_ascci[i], "", end="")
        input()

        # Criptografar: C = M^e mod n
        crip = []
        for i in range(0, len(msg)):
            crip.append((msg_ascci[i] ** e) % n)

        print(f"\nPara criptografar a mensagem, utilizamos C = M^e mod n para cada número:\n"
              f"> Mensagem criptografada em decimal: ", end="")
        for i in range(0, len(crip)):
            print(crip[i], "", end="")
        input()

        print(f"\nPronto! Para decriptografar, informe a mensagem criptografada ({crip}) e as chave privadas "
              f"d = {d} e n = {n}.\n\n")
    if op == 'D':  # DECRIPTOGRAFAR
        print("Escolhido: (D) - Decriptografia")
        print("\nPara decriptografar pelo método RSA, deve-se saber as chaves privadas (d, n).")
        input()

        crip = input("Digite a mensagem a ser decriptografada: ").split()
        for i in range(0, len(crip)):
            crip[i] = int(crip[i])
        d = int(input("Digite a chave privada d: "))
        n = int(input("Digite a chave privada n: "))

        decrip = []
        for i in range(0, len(crip)):
            decrip.append((crip[i] ** d) % n)
        dascci = []
        for i in range(0, len(decrip)):
            dascci.append(chr(decrip[i]))

        print("\nMensagem decriptografada: ", decrip)
        print("Mensagem decriptografada: ", dascci)

    print("\n(C) - CRIPTOGRAFAR\n(D) - DECRIPTOGRAFAR\n(S) - SAIR\n")
    op = input("Digite a opção desejada: ").upper()

    while op not in 'CDS':  # Validação
        op = input("Digite (C) para Criptografar, (D) para decriptografar ou (S) para Sair ").upper()
