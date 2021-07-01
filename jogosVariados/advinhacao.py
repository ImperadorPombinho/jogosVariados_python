from random import randint
from math import fabs


def printar_igual(num=34):
    print('=' * num)


def jogar():
    pontos = 1000
    tentativas = 0

    printar_igual(50)
    print('Bem-vindo ao jogo de Adivinhação!')
    print()
    print('Qual o nivel de dificuldade ? ')
    print('(1) Fácil\n(2) Médio\n(3) Difícil')
    printar_igual(50)

    erro = True
    while erro:
        nivel = int(input('Escolha: '))
        erro = False
        if nivel == 1:
            tentativas = 20
        elif nivel == 2:
            tentativas = 10
        elif nivel == 3:
            tentativas = 5
        else:
            print('Erro ao escolher nivel')
            erro = True
    numero_secreto = randint(1, 100)

    for rodadas in range(1, tentativas + 1):
        print(f'Tentativa {rodadas} de {tentativas}')
        numero_usuario = int(input('Me de um numero de 1 a 100, usuario: '))
        print('Você digitou esse numero: ', numero_usuario)

        if numero_usuario > 100 or numero_usuario < 1:
            print('Voce digitou o numero errado, digite apenas entre 1 a 100')
            continue
        acertou = numero_usuario == numero_secreto
        foi_maior = numero_usuario > numero_secreto
        foi_menor = numero_usuario < numero_secreto

        if acertou:
            print('Acertou')
            break
        elif foi_maior:
            print('Seu chute foi maior que o numero secreto')
        elif foi_menor:
            print('Seu chute foi menor que o numero secreto')
        pontos_perdidos = fabs(numero_secreto - numero_usuario)
        pontos -= pontos_perdidos
        print(f'Seus pontos: {int(pontos)}')
    print('Fim do Jogo')
    print(f'Ao final do jogo seus pontos foram: {pontos}')


if __name__ == '__main__':
    jogar()
