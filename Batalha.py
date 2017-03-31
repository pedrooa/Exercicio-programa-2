
def Batalha(meu,p,oponente):
    import json
    global InsperDex
    InsperDex = []
    with open('inspermons.json') as arquivo:
        Inspermons = json.load(arquivo)
    print("Voce se deparou um um {0} selvagem!".format(Inspermons[oponente]['nome']))
    if Inspermons[oponente] not in InsperDex:
        InsperDex.append(Inspermons[oponente])
    while meu['vida'] > 0 and Inspermons[oponente]['vida']>0:
        Inspermons[oponente]['vida'] = Inspermons[oponente]['vida'] - meu['poder'] + Inspermons[oponente]['defesa']
        if Inspermons[oponente]['vida'] <= 0:
            print("Você derrotou seu oponente!")
            print("A vida de seu Ipmon restante é: {0}".format(meu['vida']))
        else:
            meu['vida'] = meu['vida'] - Inspermons[oponente]['poder'] + meu['defesa']
            #o print funciona mas quando retorna Verdadeiro o if do ep02 não funciona
            if meu['vida'] <= 0:
                print("Você foi derrotado!")
                return True
