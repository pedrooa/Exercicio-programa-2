#Ep02 - Inspermon
import random
import json
from Batalha import Batalha

#Mostrar os tres pokemons iniciais em ordem numero de 0-2, para depois o usuario escolher qual deseja
def inspermon_inicial(ipmon_inicial):
    return Inspermons[ipmon_inicial]

def mostra_inspermon(p):
    print('\n Inspermon : {0}'. format(Inspermons[p]['nome']))
    print('Poder = {0}'. format(Inspermons[p]['poder']))
    print('Defesa = {0}'. format(Inspermons[p]['defesa']))
    print('Vida =  {0} \n'. format(Inspermons[p]['vida']))


with open('inspermons.json') as arquivo:
    Inspermons = json.load(arquivo)

Insperdex = []

while True:
    açao_usuario = int(input('\nVocê pode andar e procurar Inspermons ou dormir para recuperar sua vida. \nDigite 1 para andar ou 0 para dormir: '))
    if açao_usuario == 0:
        print('\n Dormindo!')
        break #O jogo acaba quando o jogador vai dormir
    elif açao_usuario == 1:
        print('\n Andando...')
        p = int(input('\nQual InsperMon deseja usar: \nCharmander (0) \nSquirtle (1) \nBulbasaur(2)\n'))#obs: funciona com outros pokemons se o jogador escolher numeros acima de 2
        meu = inspermon_inicial(p)
        if meu['nome'] not in Insperdex:
            Insperdex.append(meu['nome'])
        print("\nStats iniciais de seu InsperMon: \n{0}".format(meu))
        oponente = random.randrange(len(Inspermons))
        if Inspermons[oponente]['nome'] not in Insperdex:
            Insperdex.append(Inspermons[oponente]['nome'])
        Batalha(meu,p, oponente,Inspermons)
        hp = int(input("Bem Vindo ao helpdesk! Digite (1) para recuperar a vida de seu Inspermon, ou (0) para continuar: "))
        if hp ==1:
            meu["vida"] = Inspermons[p]["vida"]
        if meu["xp"] >= 50:
            print("Seu InsperMon está evoluindo!")
            meu["xp"] = 0
            meu["poder"] +=15
            meu["vida"] += 100
            meu["defesa"] +=5
        print('\nSeu InsperDex é este:\n{0}'. format(Insperdex))
