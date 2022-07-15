from unittest.mock import CallableMixin
from par_impar_tools import *

class Adversario:
    def __init__(self, nome= input("Qual seu nome?")):
        self.nome = nome
        #nome = input("Qual seu nome?")
    

        #joao voce venceu.
    def par_ou_impar (self, txt="Escolha entre PAR ou IMPAR:"):
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

    def validacao(self, txt="Escolha um numero para nossa brincadeira:"):
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


    def jogada_player2(self):
        """Jogada do computador, mostra o numero que o pc escolheu."""
        player2_jogada = random.randint(0,5)
        print(f"Número escolhido pelo player:{player2_jogada}")
        return player2_jogada



    def resultado(self, player1, player2, resposta_par_impar):
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


    def joga_par_ou_impar(self):
        
        resposta_par_impar = self.par_ou_impar()
        player1 = self.validacao()
        player2 = self.jogada_player2()
        final = self.resultado(player1, player2, resposta_par_impar)
        return final
        


    def campeonato(self, nome):
        n = int(input("Quantas vezes gostaria de jogar?"))
        player1 = 0
        player2 = 0
        for competir in range(n):
            final = self.joga_par_ou_impar()

            if final == 0:
                player1 = player1 +1 
                
            else:
                player2 = player2 +1
        if player1 > player2:
            print (f"{nome} ganhou {player1} vezes.")
        elif player1 == player2:
            print (f"{nome} empatou com {player1} a {player2}.")
        elif player1 < player2:
            print (f"Que pena {nome} perdeu de {player1} a {player2}.") 


    

        

jogo = Adversario()
print (jogo.nome)

jogo.campeonato(jogo.nome)


#@classmethod
    #def tudo(self):
        #return self.tudo()