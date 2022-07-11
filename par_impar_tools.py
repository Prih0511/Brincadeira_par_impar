import random


if __name__ == "__main__":

    def comeco_brincadeira(txt="Olá, vamos brincar de par ou impar? 'DIGITE 0 PARA SAIR'."):
        vamos_jogar = ""   
        while vamos_jogar != 0:
            vamos_jogar = input(txt)
        
            print("Ok, VAMOS LÁ!!!")
        

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


    #uma funcao global
    resposta_par_impar = par_ou_impar()


    def validacao(txt="Escolha um numero para nossa brincadeira:"):
        """Numero do jogador, valida se é inteiro.
        É esperado uma string de parametro
        e mostra o numero que o jogador escolheu."""
        player1_jogada = input(txt)

        if not player1_jogada.isdecimal:
            print("Numero invalido, tente outro:")
        elif player1_jogada < "0":
            print("Voce digitou um numero negativo. tente com um positivo agora:")

        print(f"O numero escolhido foi {player1_jogada}:")
        return player1_jogada

    #funcao global
    player1 = validacao()


    def jogada_player2():
        """Jogada do computador, mostra o numero que o pc escolheu."""
        player2_jogada = random.randint(0,5)
        print(f"Número escolhido pelo player:{player2_jogada}")
        return player2_jogada


    #funcao global + soma
    player2 = jogada_player2()


    def resultado(player1, player2, resposta_par_impar):
        """importando as paradar de cima e respondendo o usuario. sao esperados o varores de
        player1 e 2 e resposta_par_impar"""

        soma = int(player1) + player2

        resultado = ""

        if soma%2 == 0:
            resultado == "par_ganha"
            print("Par ganhou!")
        else:
            print("Ímpar ganhou!")


        if resposta_par_impar == "par" and resultado == "par_ganha":
            print("Deu PAR, você ganhoou!!")
            return "Você venceu!"

        elif resposta_par_impar == "impar" and resultado == "":
            print("Deu IMPAR, você ganhou!!")
            return "Você venceu!"

        else:
            print("Que pena. Game Over")
            return "Você perdeu!"







