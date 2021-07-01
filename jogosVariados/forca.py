from random import choice


def remove_posicao(lista, posicao):
    for ind in range(0, len(lista)):
        if ind == posicao and lista[ind] == '_':
            lista.pop(posicao)
    return lista


def achar_letra(indice, palavra_secreta):
    for letra in palavra_secreta:
        if letra == palavra_secreta[indice]:
            return letra
    return -1


def preenche_palavra(indice, lista_palavra_secreta, palavra_secreta):
    for c in range(0, len(indice)):
        letra_inserir = achar_letra(indice[c], palavra_secreta)
        lista_palavra_secreta = remove_posicao(lista_palavra_secreta, indice[c])
        lista_palavra_secreta.insert(indice[c], letra_inserir)
    return lista_palavra_secreta


def encontrou_letra(letra, palavra):
    indice = []
    for ind, let in enumerate(palavra):
        if let == letra:
            indice.append(ind)
    return indice


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_lista(lista):
    for ind in range(0, len(lista)):
        if ind == len(lista) - 1:
            print(lista[ind])
        else:
            print(lista[ind], end='')


def preenche_lista(palavra_secreta):
    lista = ['_' for letra in palavra_secreta]
    return lista


def printar_igual(num=33):
    print('=' * num)


def ler_arquivo():
    lista = []
    with open('frutas.txt', 'r') as arquivo:
        for linha in arquivo:
            lista.append(linha.strip())
    return lista


def jogar():
    printar_igual()
    print('Bem vindo ao jogo forca')
    printar_igual()
    dados_palavras = ler_arquivo()
    palavra_secreta = choice(dados_palavras).upper()
    enforcou = False
    acertou = False
    preenche = preenche_lista(palavra_secreta)
    imprime_lista(preenche)
    tentativas = 0
    while not enforcou and not acertou:
        print('Jogando...')
        print(f'Erros: {tentativas}')
        letra = input('Digite uma letra usuario: ').strip().upper()
        if letra in palavra_secreta:
            print('Letra encontrada')
            indice = encontrou_letra(letra, palavra_secreta)
            preenche = preenche_palavra(indice, preenche, palavra_secreta)
        else:
            tentativas += 1
            desenha_forca(tentativas)
        imprime_lista(preenche)
        acertou = '_' not in preenche
        enforcou = tentativas == 7
    if acertou:
        imprime_mensagem_vencedor()
    elif enforcou:
        imprime_mensagem_perdedor(palavra_secreta)
    print(f'Tentativas: {tentativas}')
    print('Fim de jogo')


if __name__ == '__main__':
    jogar()
