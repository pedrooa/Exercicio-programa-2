#Ep02 - Inspermon
import random, json, sys, time, funções
from colorama import Fore, Back, Style
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
meus_ipmon = lista_meus_ipmons(Inspermons)

while True:
    açao_usuario = int(input('\nVocê pode andar e procurar Inspermons ou dormir para recuperar sua vida. \nDigite 1 para andar ou 0 para dormir: '))
    if açao_usuario == 0:
        print(Style.GREEN + '\n Dormindo!')
        break #O jogo acaba quando o jogador vai dormir
    elif açao_usuario == 1:
        string = "\nAndando ...\n"
        escrita_timer(string)

        #obs: funciona com outros pokemons se o jogador escolher numeros acima de 2
        p = int(input('\nQual InsperMon deseja usar: \nCharmander (0) \nSquirtle (1) \nBulbasaur(2)\n'))#meus_ipmon[p] = inspermon_inicial(p)

        if meus_ipmon[p]['nome'] not in Insperdex:
            Insperdex.append(meus_ipmon[p]['nome'])
        print("\nStats iniciais de seu InsperMon: \n{0}".format(meus_ipmon[p]))
        oponente = random.randrange(len(Inspermons))

        if Inspermons[oponente]['nome'] not in Insperdex:
            Insperdex.append(Inspermons[oponente]['nome'])
        Batalha(meus_ipmon[p],p, oponente,Inspermons)

        while True:
            hp = int(input("\nBem Vindo ao helpdesk! Digite (1) para recuperar a vida de seu Inspermon, ou (0) para continuar: "))
            if hp ==1 or hp ==0:
                break
            else:
                print('\nEscreva direito!')

        print(meus_ipmon[p]["vida"])
        print(Inspermons[p]["vida"])

        if hp == 1:
            meus_ipmon[p]["vida"] = Inspermons[p]["vida"]
            print(meus_ipmon[p])

        if meus_ipmon[p]["xp"] >= 50:
            print("\nSeu InsperMon está evoluindo!")
            meus_ipmon[p]["xp"] = 0
            meus_ipmon[p]["poder"] +=15
            meus_ipmon[p]["vida"] += 100
            meus_ipmon[p]["defesa"] +=5
        print('\nSeu InsperDex é este:\n{0}'. format(Insperdex))

    else:
        print("\nCódigo incorreto, redigite!")
