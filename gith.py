'''
     Algoritmo de Criptografia em RSA (Com Cores de Destaque).

     Integrantes do Grupo: Caio Costa Martins (Ciências da Computação), João Gabriel Almeida dos Santos e Vitor Hugo Gumercindo da Silva (Sistemas de Informação).

     Responsável pela Criação: João Gabriel Almeida dos Santos.

     Função: O algoritmo tem como função a geração e utilização de chaves para criptografar e descriptografar mensagens utilizando a técnica de criptografia RSA com codificação na tabela ASCII.
'''
import random

sair = 1

# Menu de Opções.

while sair == 1:

    print("")
    print("\033[33m******* Criptografadora RSA *******")
    print("********** Menu de Ações **********\033[m")
    print("")
    print("1 - Criar chaves para RSA manualmente.")
    print("2 - Criar chaves para RSA automaticamente.")
    print("3 - Criptografar uma mensagem.")
    print("4 - Descriptografar uma mensagem.")
    print("5 - Encerrar programa.")
    print("")
    menu = int(input("O que deseja fazer? "))
    print("")

    if menu == 5:
        print("\033[33mPrograma Encerrado.\033[m")
        print("")
        sair = 0

    if menu < 1 or menu > 5:
        print("\033[31mErro. Ação inválida.")
        print("Tente novamente.\033[m")
        print("")

    # Todo esse bloco é para a geração das chaves, processo essencial na estrutura e aplicação do RSA.

    # Definir as chaves.

    if menu == 1:
        # Definir os valores de p e q que devem ser necessariamente números primos.
        print("\033[33m********** Criação das Chaves **********\033[m")
        print("")
        while True:
            while True:
                p = int(input("Insira qualquer valor primo para P: "))
                pstr = str(p)
                if len(pstr) < 2:
                    print("")
                    print("\033[31mInsira valores com pelo menos 2 caracteres.\033[m")
                    print("")
                else:
                    total = 0
                    for c in range(1, p + 1):
                        if p % c == 0:
                            total += 1
                    if total == 2:
                        break
                    else:
                        print("")
                        print("\033[31mO valor inserido não é primo, digite novamente.\033[m")
                        print("")

            while True:
                q = int(input("Insira qualquer valor primo para Q: "))
                qstr = str(q)
                if len(qstr) < 2:
                    print("")
                    print("\033[31mInsira valores com pelo menos 2 caracteres.\033[m")
                    print("")
                elif p == q:
                    print("")
                    print("\033[31mP e Q não podem ser iguais.\033[m")
                    print("")
                else:
                    total = 0
                    for c in range(1, q + 1):
                        if q % c == 0:
                            total += 1
                    if total == 2:
                        break
                    else:
                        print("")
                        print("\033[31mO valor inserido não é primo, digite novamente.\033[m")
                        print("")

            # Determinar o produto de p e q: n = (p * q).

            n = (p * q)

            # Determinar a função totiente de n: fn = (p - 1) * (q - 1).
            fn = (p - 1) * (q - 1)
            print("")
            print(f"A função totiente f(n) = {fn}")
            print("")

            # Definir o valor de e, onde e tem que satisfazer: MDC(f(n), e) = 1, sendo e > 1.
            while True:
                e = int(
                    input("Insira um valor para E, que esteja entre 1 e f(n) que seja co-primo em relação a f(n): "))
                if e > 1 and e < fn:
                    mdc = e
                    while e % mdc != 0 or fn % mdc != 0:  # Processo de determinação do MDC(f(n), e) = 1.
                        mdc = mdc - 1
                    if mdc == 1:
                        break
                    else:
                        print("")
                        print("\033[31mO valor inserido não é válido.\033[m")
                        print("")
                else:
                    print("")
                    print("\033[31mO valor inserido não é válido.\033[m")
                    print("")

            # Determinar o inverso multiplicativo de e mod f(n) = d, onde d deve satisfazer: d * e ≡ 1 mod f(n).
            for d in range(1, fn, 1):
                if d * e % fn == 1:
                    break

            if e == d:
                print("")
                print(
                    "\033[31mErro na criação das chaves.")  # As chaves E e D não podem ser iguais, pois da erro na hora de criptografar e descriptografar.
                print("Tente outros valores.\033[m")
                print("")

            if e != d:
                print("")
                print("\033[32m********** Chaves Calculadas! **********")
                print(f"Chaves Públicas: N = {n}; E = {e}")
                print(f"Chaves Privadas: P = {p}; Q = {q}; D = {d}")
                print("")
                print("Ação Finalizada.")
                print("Retornando ao Menu.\033[m")
                print("")
                break

    if menu == 2:
        # Definir os valores de p e q que devem ser necessariamente números primos.
        while True:
            while True:
                p = random.randrange(100, 999)
                total = 0
                for c in range(1, p + 1):
                    if p % c == 0:
                        total += 1
                if total == 2:
                    break

            while True:
                q = random.randrange(100, 999)
                if p != q:
                    total = 0
                    for c in range(1, q + 1):
                        if q % c == 0:
                            total += 1
                    if total == 2:
                        break

            # Determinar o produto de p e q: n = (p * q).
            n = (p * q)

            # Determinar a função totiente de n: fn = (p - 1) * (q - 1).
            fn = (p - 1) * (q - 1)

            # Definir o valor de e, onde e tem que satisfazer: MDC(f(n), e) = 1, sendo e > 1.
            while True:
                e = random.randrange(2, fn - 1)
                mdc = e
                while e % mdc != 0 or fn % mdc != 0:  # Processo de determinação do MDC(f(n), e) = 1.
                    mdc = mdc - 1
                if mdc == 1:
                    break
                    # Determinar o inverso multiplicativo de e mod f(n) = d, onde d deve satisfazer: d * e ≡ 1 mod f(n).
            for d in range(1, fn, 1):
                if d * e % fn == 1:
                    break

            if e != d:
                print("")
                print("\033[32m********** Chaves Calculadas! **********")
                print(f"Chaves Públicas: N = {n}; E = {e}")
                print(f"Chaves Privadas: P = {p}; Q = {q}; D = {d}")
                print("")
                print("Ação Finalizada.")
                print("Retornando ao Menu.\033[m")
                print("")
                break

    # Processo de Criptografia.
    if menu == 3:
        print("\033[33m********** Criptografando uma Mensagem **********\033[m")
        print("")
        msg_final = []
        msg_final_string = str
        x = 0
        n = int(input("Insira a chave pública N: "))
        e = int(input("Insira a chave pública E: "))
        print("")
        msg = input("Insira a mensagem que deseja criptografar:\n")
        msg_precode = [ord(c) for c in
                       msg]  # Essa linha codifica a mensagem de caracteres normais que foi digitada para a tabela ASCII.

        print("")
        print("\033[33mAguarde, a Mensagem está sendo Criptografada...\33[m")
        while True:
            cripto = ((msg_precode[
                           x] ** e) % n)  # Cada elemento da 'msg_precode' é criptografado usando RSA e sendo colocado em forma de lista na variavel 'cripto'.
            msg_final.append(
                cripto)  # Cada elemento de 'cripto', já criptografado, esta sendo adicionado ao final da lista 'msg_final', fazendo com que a mensagem criptografada fique na ordem correta.
            x += 1

            if len(msg_final) == len(
                    msg_precode):  # Essa condição é feita para parar o while, nada mais é que, quando o número de elementos da 'msg_final'(RSA) for equivalente ao número de elementos da
                break  # 'msg_precode'(ASCII) o while ira parar porque não existe mais elementos para ser criptografado.

        msg_final_string = ' '.join(map(msg_final_string,
                                        msg_final))  # Essa linha converte a 'msg_final' que é uma lista para string na 'msg_final_string', além de substituir as virgulas da lista por espaços.

        print("")
        print("\033[32m********** Mensagem Criptografada! **********")
        print(msg_final_string)
        print("")
        print("Ação Finalizada.")
        print("Retornando ao Menu.\033[m")
        print("")

    # Processo de Descriptografia.
    if menu == 4:
        print("\033[33m********** Descriptografando uma Mensagem **********\033[m")
        print("")
        x = 0
        msg_final_descripto = []
        p = int(input("Insira a chave privada P: "))
        q = int(input("Insira a chave privada Q: "))
        d = int(input("Insira a chave privada D: "))
        n = p * q
        print("")
        msg_cripto = input("Insira a mensagem que deseja descriptografar:\n")
        msg_cripto = msg_cripto.split()
        msg_cripto_lista = []  # Processo para converter uma string em lista.
        for elemento in msg_cripto:
            msg_cripto_lista.append(int(elemento))

        print("")
        print("\033[33mAguarde, a Mensagem está sendo Descriptografada...\33[m")
        while True:
            descripto = ((msg_cripto_lista[
                              x] ** d) % n)  # Após converter a string em lista repete-se o mesmo processo da criptografia, mas agora para descriptografar.
            msg_final_descripto.append(descripto)
            x += 1
            if x == len(
                    msg_cripto_lista):  # Novamente esse condição é feita para parar o while, quando o x for igual o número de elementos da 'msg_cripto_lista' o while para, o x é o indicador de
                break  # elementos que se usa na primeira linha deste while.

        msg_original = ''.join(map(chr,
                                   msg_final_descripto))  # Após a mensagem em RSA ser descriptografada retornando a ser ASCII, esta linha decodifica de ASCII para texto normal.

        print("")
        print("\033[32m********** Mensagem Descriptografada! **********")
        print(msg_original)
        print("")
        print("Ação Finalizada.")
        print("Retornando ao Menu.\033[m")
        print("")