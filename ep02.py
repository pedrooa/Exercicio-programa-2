#Ep02 - Inspermon
import random, json
from funções import *
from colorama import Fore, Back, Style
from Batalha import Batalha


def mostra_insperdex(Insperdex):
    for e in Insperdex:
        print(e)


with open('inspermons.json') as arquivo:
    Inspermons = json.load(arquivo)

Insperdex = []
meus_ipmon = lista_meus_ipmons(Inspermons)

Checkpoint = [meus_ipmon]  #Prevenção de erros caso o jogador tente dar Save sem ter jogado nada.

load = int(input('\nDeseja carregar um jogo existente?\n1   -   Sim\n2   -   Nao\n'))
while True:
    if load == 1:
        with open('SaveGame.json','r') as arquivo:
            dados = json.load(arquivo)
        meus_ipmon = dados[0]
        Insperdex = dados[1]
        break
    elif load == 2:
        break
    else:
        print('Codigo Inexistente!')

while True:
    açao_usuario = int(input('\nVocê pode andar e procurar Inspermons ou dormir para recuperar sua vida. \nDigite 1 para andar ou 0 para dormir: '))
    if açao_usuario == 0:
        #Pergunta ao usuário se quer salvar o jogo
        save = int(input('\nDeseja salvar seu progresso?(Obs : Isso vai deletar seu save passado)\n1   -   Sim\n2   -   Nao\n'))
        if save == 1:
            with open('SaveGame.json','w') as arquivo:
                json.dump(Checkpoint,arquivo)
            print('\nJogo salvo com sucesso!\nDormindo!')
            break
        elif save ==2:
            print('\n Dormindo!')
            break
        else:
            print('Codigo inexistente!')
    elif açao_usuario == 1:
        #Pergunta ao usuário qual inspermon ele quer usar
        p = inspermon_usuario(meus_ipmon)

        #Armazena a vida inicial do ipmon
        vida = meus_ipmon[p]['vida']

        #Roda a função timer para a string
        string = "\nAndando ...\n"
        escrita_timer(string)

        #Adiciona os Inspermons ao Insperdex
        if meus_ipmon[p]['nome'] not in Insperdex:
            Insperdex.append(meus_ipmon[p]['nome'])
        
        oponente = random.randrange(len(Inspermons))
        if Inspermons[oponente]['nome'] not in Insperdex:
            Insperdex.append(Inspermons[oponente]['nome'])
        print("\nStats iniciais de seu InsperMon: \nInspermon : {0}\nPoder = {1}\nVida = {2}\nDefesa = {3}\nXp = {4}".format(meus_ipmon[p]['nome'],meus_ipmon[p]['poder'],meus_ipmon[p]['vida'],meus_ipmon[p]['defesa'],meus_ipmon[p]['xp']))
        #Batalha entre os Inspermons
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



        if meus_ipmon[p]["xp"] >= 50:
            print("\nSeu InsperMon está evoluindo!")
            meus_ipmon[p]["xp"] = 0
            meus_ipmon[p]["poder"] +=15
            meus_ipmon[p]["vida"] += 100
            meus_ipmon[p]["defesa"] +=5


        #print('\nSeu InsperDex é este:{0}'.format(print(mostra_insperdex(Insperdex))))
        print('\nSeu Insperdex é:')
        mostra_insperdex(Insperdex)
        Checkpoint = [meus_ipmon,Insperdex]

    else:
        print("\nCódigo incorreto, redigite!")
