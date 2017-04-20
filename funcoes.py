import sys, time
import colorama
from colorama import Fore, Back, Style, init

meus_ipmon = list()
init()
class funcao:
    def lista_meus_ipmons(Inspermons):
        for i in range(3):
            meus_ipmon.append(Inspermons[i])
        return meus_ipmon

    def escrita_timer(estringue, n=0.03):
        for char in estringue:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(n)

    def poder_tipo_Inspermon(meu, Inspermons, oponente):
        if meu['tipo']=='Agua':
            if Inspermons[oponente]['tipo'] == 'Fogo':
                meu['poder'] *= 1.6
                print("\nOs ataques de seu Inspermon vão ser super efetivos contra esse Inspermon tipo Fogo!\n")
            elif Inspermons[oponente]['tipo'] == 'Ar':
                Inspermons[oponente]['poder'] *=1.6
                print("\nCuidado! Os ataques desse oponente do tipo Ar serão super efetivos contra o seu Inspermon!\n")

        elif meu['tipo']=='Fogo':
            if Inspermons[oponente]['tipo']== 'Terra':
                meu['poder'] *= 1.6
                print("Os ataques de seu Inspermon vão ser super efetivos contra esse Inspermon tipo Terra!")
            elif Inspermons[oponente]['tipo'] == 'Agua':
                Inspermons[oponente]['poder'] *=1.6
                print("\nCuidado! Os ataques desse oponente do tipo Agua serão super efetivos contra o seu Inspermon!\n")

        elif meu['tipo']=='Ar':
            if Inspermons[oponente]['tipo'] == 'Agua':
                meu['poder'] *= 1.6
                print("\nOs ataques de seu Inspermon vão ser super efetivos contra esse Inspermon tipo Agua!\n")
            elif Inspermons[oponente]['tipo'] == 'Terra':
                Inspermons[oponente]['poder'] *=1.6
                print("\nCuidado! Os ataques desse oponente do tipo Terra serão super efetivos contra o seu Inspermon!\n")

        elif meu['tipo']=='Terra':
            if Inspermons[oponente]["tipo"] == 'Ar':
                meu['poder'] *= 1.6
                print("\nOs ataques de seu Inspermon vão ser super efetivos contra esse Inspermon tipo Ar!\n")
            elif Inspermons[oponente]['tipo'] == 'Fogo':
                Inspermons[oponente]['poder'] *=1.6
                print("\nCuidado! Os ataques desse oponente do tipo Fogo serão super efetivos contra o seu Inspermon!\n")

    #Função não utilizada
    def mostra_inspermon(Inspermons,p):
        print('\n Inspermon : {0}'. format(Inspermons[p]['nome']))
        print('Poder = {0}'. format(Inspermons[p]['poder']))
        print('Defesa = {0}'. format(Inspermons[p]['defesa']))
        print('Vida =  {0}\n'. format(Inspermons[p]['vida']))

    def inspermon_inicial(ipmon_inicial):
        return Inspermons[ipmon_inicial]

    #Corrige a vida negativa dos Inspermons
    def correcao_vida(Inspermons, p):
        if Inspermons[p]['vida'] <= 0:
            Inspermons[p]['vida'] = 0
        return Inspermons[p]['vida']

    def mostra_insperdex(Insperdex_nome):
        for e in Insperdex_nome:
                print(e['nome'])
                print('Poder = {0}'. format(e['poder']))
                print('Defesa = {0}'. format(e['defesa']))
                print('Vida = {0:.2f}\n'. format(e['vida']))
                print('Tipo: {0}'. format(e['tipo']))

    #Determina qual ipmon inicial
    def inspermon_usuario(Inspermons):
        charm = Inspermons[0]['nome']
        squir = Inspermons[1]['nome']
        bulb = Inspermons[2]['nome']
        vari = True
        while vari:
            print(Fore.YELLOW)
            p = int(input('\nQual InsperMon deseja usar: \n{0} (0) \n{1} (1) \n{2} (2)\n'.format(charm,squir,bulb))) #meus_ipmon[p] = inspermon_inicial(p)
            if p == 0 or p == 1 or p == 2 and Inspermons[p]['vida'] != 0:
                vari = False
                return p
            else:
                if Inspermons[p]['vida'] == 0:
                    print("\nEste Inspermon não está mais entre nós. Escolha outro\n")
                else:
                    print('\nDigite o numero referente ao pokemon que deseja, corretamente.')
