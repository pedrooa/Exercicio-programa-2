import random
perdeu = False#Se perder a batalha, perdeu = True
InsperDex=[]
oponente = random.randrange(12)#Encontra um pokemon aleatorio
def Batalha(meu,oponente):
    print("Voce se deparou um um {0} selvagem!".format(Inspermons[oponente][nome]))
    if Inspermons[oponente] not in InsperDex:
        InsperDex.append(Inspermons[oponente])
    while Inspermons[meu][vida] > 0 and Inspermons[oponente][vida]>0:
        Inspermons[oponente][vida] = Inspermons[oponente][vida] - Inspermons[meu][ataque] + Inspermons[oponente][defesa]
        if ipmon[oponente][vida] <= 0:
            return("Você derrotou seu oponente!")
        else:
            Inspermons[meu][vida] = Inspermons[meu][vida] - Inspermons[oponente][ataque] + Inspermons[meu][defesa]
            if Inspermons[meu][vida] <= 0:
                return("Você foi derrotado!")
                global perdeu
                perdeu = True
