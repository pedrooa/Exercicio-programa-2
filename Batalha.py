import json, colorama, random

traço = "------"*15

def Batalha(meu,p,oponente,Inspermons):
    print("\nVoce se deparou com um {0} selvagem!".format(Inspermons[oponente]['nome']))
    fuga = int(input('\nDeseja fugir da batalha? (1) Sim e (2) Não \n'))
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
    elif fuga == 2:
        while meu['vida'] > 0 and Inspermons[oponente]['vida']>0:
            e = 1
            print('\n' + traço + '\n')
            print("\nRound {0} :" .format(e))
            print("O {0} possui {1} de vida  ---- O {2} possui {3} de vida" .format(meu['nome'], meu['vida'], Inspermons[oponente]['nome'], Inspermons[oponente]['vida']))
            e += 1
            Inspermons[oponente]['vida'] = Inspermons[oponente]['vida'] - meu['poder'] + Inspermons[oponente]['defesa']
            if Inspermons[oponente]['vida'] <= 0:
                print("\nVocê derrotou seu oponente!")
                print("A vida de seu Ipmon restante é: \n{0}".format(meu['vida']))
                meu["xp"] +=10
            else:
                meu['vida'] = meu['vida'] - Inspermons[oponente]['poder'] + meu['defesa']
                if meu['vida'] <= 0:
                    print("\nVocê foi derrotado!")

                    #return True #Não sei se há necessidade disso
