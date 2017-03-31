
def Batalha(meu,p,oponente,Inspermons):
    import json
    global InsperDex
    InsperDex = []
    print("\nVoce se deparou com um {0} selvagem!".format(Inspermons[oponente]['nome']))
    fuga = input('\nDeseja fugir da batalha? (1) Sim e (0) Não \n')
    if fuga == 1:
        print('\nVocê fugiu da batalha!')
    elif fuga == 0:
        if Inspermons[oponente] not in InsperDex:
            InsperDex.append(Inspermons[oponente])
        while meu['vida'] > 0 and Inspermons[oponente]['vida']>0:
            Inspermons[oponente]['vida'] = Inspermons[oponente]['vida'] - meu['poder'] + Inspermons[oponente]['defesa']
            if Inspermons[oponente]['vida'] <= 0:
                print("\nVocê derrotou seu oponente!")
                print("A vida de seu Ipmon restante é: \n{0}".format(meu['vida']))
            else:
                meu['vida'] = meu['vida'] - Inspermons[oponente]['poder'] + meu['defesa']
                #o print funciona mas quando retorna Verdadeiro o if do ep02 não funciona
                if meu['vida'] <= 0:
                    print("\nVocê foi derrotado!")
                    return True
