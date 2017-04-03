from Insperdex import mostra_Insperdex as Insperdex
import json
import random

def Batalha(meu,p,oponente,Inspermons):
    print("\nVoce se deparou com um {0} selvagem!".format(Inspermons[oponente]['nome']))
    fuga = int(input('\nDeseja fugir da batalha? (1) Sim e (0) Não \n'))
    if fuga == 1:
        n = random.random()
        if n<=0.51:
            print('\nVocê fugiu da batalha!')
        else:
            print('\nFuga sem sucesso!')
            while meu['vida'] > 0 and Inspermons[oponente]['vida']>0:
                Inspermons[oponente]['vida'] = Inspermons[oponente]['vida'] - meu['poder'] + Inspermons[oponente]['defesa']
                if Inspermons[oponente]['vida'] <= 0:
                    print("\nVocê derrotou seu oponente!")
                    print("A vida de seu Ipmon restante é: \n{0}".format(meu['vida']))
                    meu['xp'] +=10
                else:
                    meu['vida'] = meu['vida'] - Inspermons[oponente]['poder'] + meu['defesa']
                    if meu['vida'] <= 0:
                        print("\nVocê foi derrotado!")
    elif fuga == 0:
        while meu['vida'] > 0 and Inspermons[oponente]['vida']>0:
            Inspermons[oponente]['vida'] = Inspermons[oponente]['vida'] - meu['poder'] + Inspermons[oponente]['defesa']
            if Inspermons[oponente]['vida'] <= 0:
                print("\nVocê derrotou seu oponente!")
                print("A vida de seu Ipmon restante é: \n{0}".format(meu['vida']))
                meu["xp"] +=10
            else:
                meu['vida'] = meu['vida'] - Inspermons[oponente]['poder'] + meu['defesa']
                if meu['vida'] <= 0:
                    print("\nVocê foi derrotado!")
<<<<<<< HEAD
                    #return True #Não sei se há necessidade disso
=======
>>>>>>> 18e28764bb72d3ad405f808dc815b38e68324108
