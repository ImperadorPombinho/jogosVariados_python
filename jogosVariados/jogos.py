import forca
import advinhacao


def printar_igual(num=33):
    print('='*num)


def escolhe_jogo():
    printar_igual()
    print('Escolha o seu jogo')
    print('(1) forca\n(2) advinhação')
    printar_igual()
    jogo = int(input('Digite: '))

    if jogo == 1:
        print('Jogando a forca')
        forca.jogar()

    elif jogo == 2:
        print('Jogando a advinhação')
        advinhacao.jogar()


if __name__ == '__main__':
    escolhe_jogo()
