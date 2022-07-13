import random


if __name__ == "__main__":
#usuario escolher entre par ou impar e restornar oque ele escolheu na tela.
    def par_ou_impar (txt="Escolha entre PAR ou IMPAR:"):
        perguntar_par_impar = ""
        while perguntar_par_impar != "par" and perguntar_par_impar != "impar":
            perguntar_par_impar = input(txt).lower().strip()
#se perguntar_par_impar for diferente de par ou impar, pergunte sempre.
        if perguntar_par_impar == "par":
            print("Você escolheu PAR.")
            return "par"
        else: 
            print("Você escolheu IMPAR.")
            return "impar"


#uma variavel global
    resposta_par_impar = par_ou_impar()


    def validacao(txt="Escolha um numero para nossa brincadeira:"):
        """Numero do jogador, valida se é inteiro.
        É esperado uma string de parametro
        e mostra o numero que o jogador escolheu."""
        while True:
            player1_jogada = input(txt).strip()

            if not player1_jogada.isdecimal():
                print("Numero invalido, tente outro:")
            else:
                break

        print(f"O numero escolhido foi {player1_jogada}:")
        return player1_jogada

#variavel global
    player1 = validacao()


    def jogada_player2():
        """Jogada do computador, mostra o numero que o pc escolheu."""
        player2_jogada = random.randint(0,5)
        print(f"Número escolhido pelo player:{player2_jogada}")
        return player2_jogada


#variavel global
    player2 = jogada_player2()


    def resultado(player1, player2, resposta_par_impar):
        """importando as paradar de cima e respondendo o usuario. sao esperados o valores de
        player1 e 2 e resposta_par_impar"""

        soma = int(player1) + player2

        resultado = ""

        if soma%2 == 0:
            resultado == "par_ganha"
            print(f"Resultado = {soma}")
            print("Par ganhou!")
        else:
            print(f"Resultado = {soma}")
            print("Ímpar ganhou!")


        if resposta_par_impar == "par" and resultado == "par_ganha":
            print("Deu PAR, você ganhoou!!")
            return 0

        elif resposta_par_impar == "impar" and resultado == "":
            print("Deu IMPAR, você ganhou!!")
            return 0

        else:
            print("Que pena. Game Over")
            return 1
    

    resultado(player1, player2, resposta_par_impar)

