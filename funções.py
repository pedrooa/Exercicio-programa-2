import sys, time

meus_ipmon = list()

class função():
    def lista_meus_ipmons(Inspermons):
        for i in range(3):
            meus_ipmon.append(Inspermons[i])
        return meus_ipmon

    def escrita_timer(estringue):
        for char in estringue:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.4)

    #Funções não utilizadas
    def mostra_inspermon(Inspermons,p):
        print('\n Inspermon : {0}'. format(Inspermons[p]['nome']))
        print('Poder = {0}'. format(Inspermons[p]['poder']))
        print('Defesa = {0}'. format(Inspermons[p]['defesa']))
        print('Vida =  {0}\n'. format(Inspermons[p]['vida']))

    def inspermon_inicial(ipmon_inicial):
        return Inspermons[ipmon_inicial]

    #Corrige a vida negativa dos Inspermons
    def correcao_vida(Inspermons, p):
        if Inspermons[p]['vida'] < 0:
            Inspermons[p]['vida'] = 0
            return Inspermons[p]['vida']

    def mostra_insperdex(Insperdex):
        for e in Insperdex:
            print(e)
    #Determina qual ipmon inicial
    def inspermon_usuario(Inspermons):
        charm = Inspermons[0]['nome']
        squir = Inspermons[1]['nome']
        bulb = Inspermons[2]['nome']
        vari = True
        while vari:
            p = int(input('\nQual InsperMon deseja usar: \n{0} (0) \n{1} (1) \n{2} (2)\n'.format(charm,squir,bulb))) #meus_ipmon[p] = inspermon_inicial(p)
            if p == 0 or p == 1 or p == 2 and Inspermons[p]['vida'] != 0:
                vari = False
                return p
            else:
                if Inspermons[p]['vida'] == 0:
                    print("\nEste Inspermon não está mais entre nós. Escolha outro\n")
                else:
                    print('\nDigite o numero referente ao pokemon que deseja, corretamente.')
