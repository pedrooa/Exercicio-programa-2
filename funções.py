
meus_ipmon = list()

def lista_meus_ipmons(Inspermons):
    for i in range(3):
        meus_ipmon.append(Inspermons[i] + '\n')
    return meus_ipmon

def escrita_timer(estringue):
    for char in estringue:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.4)

#Funções não utilizadas
"""def mostra_inspermon(Inspermons,p):
    print('\n Inspermon : {0}'. format(Inspermons[p]['nome']))
    print('Poder = {0}'. format(Inspermons[p]['poder']))
    print('Defesa = {0}'. format(Inspermons[p]['defesa']))
    print('Vida =  {0}\n'. format(Inspermons[p]['vida']))


def inspermon_inicial(ipmon_inicial):
    return Inspermons[ipmon_inicial]
"""
