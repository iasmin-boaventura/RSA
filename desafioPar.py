with open("par.txt", "r") as arquivo:
    vetor = arquivo.read().replace(" ", "").split()
j = 0
while j < len(vetor):
    print("j começo: ",j)
    partidas = int(vetor[j])
    player1 = vetor[j + 1]
    player2 = vetor[j + 2]
    i = j + 3
    while i < (j + 2) + partidas:
        print(i)
        mao1 = int(vetor[i][0])
        mao2 = int(vetor[i][1])
        soma = mao1 + mao2
        resto = soma % 2
        if resto == 0:
            print("par")
        else:
            print("impar")
        i += 1
    j = j + partidas + 3