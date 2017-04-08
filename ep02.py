#Ep02 - Inspermon
import random, json
from funções import *
from colorama import Fore, Back, Style
from Batalha import Batalha

with open('inspermons.json') as arquivo:
    Inspermons = json.load(arquivo)

Insperdex = []
meus_ipmon = lista_meus_ipmons(Inspermons)

while True:
    açao_usuario = int(input('\nVocê pode andar e procurar Inspermons ou dormir para recuperar sua vida. \nDigite 1 para andar ou 0 para dormir: '))
    if açao_usuario == 0:
        print('\n Dormindo!')
        break
    elif açao_usuario == 1:
        #Pergunta ao usuário qual innspermon ele quer usar
        p = inspermon_usuario(meus_ipmon)

        #Armazena a vida inicial do ipmon
        vida = meus_ipmon[p]['vida']

        #Roda a função timer para a string
        string = "\nAndando ...\n"
        escrita_timer(string)

        #Adiciona os pokemons ao Insperdex
        if meus_ipmon[p]['nome'] not in Insperdex:
            Insperdex.append(meus_ipmon[p]['nome'])
        print("\nStats iniciais de seu InsperMon: \n{0}".format(meus_ipmon[p]))
        oponente = random.randrange(len(Inspermons))
        if Inspermons[oponente]['nome'] not in Insperdex:
            Insperdex.append(Inspermons[oponente]['nome'])

        #Batalha entre os pokemons
        Batalha(meus_ipmon[p],p, oponente,Inspermons)

        #Corrige a vida do Inspermon
        correcao_vida(meus_ipmon, p)

        while True:
            hp = int(input("\nBem Vindo ao helpdesk! Digite (1) para recuperar a vida de seu Inspermon, ou (0) para continuar: "))
            if hp == 1:
                meus_ipmon[p]['vida'] = vida
                break
            elif hp == 0:
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
