from Insperdex import mostra_Insperdex as Insperdex
import json

def Batalha(meu,p,oponente,Inspermons):
    print("\nVoce se deparou com um {0} selvagem!".format(Inspermons[oponente]['nome']))
    fuga = input('\nDeseja fugir da batalha? (1) Sim e (0) Não \n')
    if fuga == 1:
        #Falta InsperDex grava o pokemon
        print('\nVocê fugiu da batalha!')
    elif fuga == 0:
        while meu['vida'] > 0 and Inspermons[oponente]['vida']>0:
            Inspermons[oponente]['vida'] = Inspermons[oponente]['vida'] - meu['poder'] + Inspermons[oponente]['defesa']
            if Inspermons[oponente]['vida'] <= 0:
                print("\nVocê derrotou seu oponente!")
                print("A vida de seu Ipmon restante é: \n{0}".format(meu['vida']))
            else:
                meu['vida'] = meu['vida'] - Inspermons[oponente]['poder'] + meu['defesa']
                #O print funciona mas quando retorna Verdadeiro o if do ep02 não funciona
                if meu['vida'] <= 0:
                    print("\nVocê foi derrotado!")
                    return True #Não sei se há necessidade disso
