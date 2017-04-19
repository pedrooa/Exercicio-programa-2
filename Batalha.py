import json, random, time
from colorama import Fore, Back, Style, init
from funcoes import funcao
init()

traço = "------"*18


def Batalha(meu,p,oponente,Inspermons):
    print(Fore.BLUE)
    print("Voce se deparou com um {0} selvagem!".format(Inspermons[oponente]['nome']))
    val = True
    if meu['tipo']=='Agua':
        if Inspermons[oponente]['tipo'] == 'Fogo':
            meu['poder'] *= 1.6
            print("\nOs ataques de seu Inspermon vão ser super efetivos contra esse Inspermon tipo Fogo!\n")
        if Inspermons[oponente]['tipo'] == 'Ar':
            Inspermons[oponente]['poder'] *=1.6
            print("\nCuidado! Os ataques desse oponente do tipo Ar serão super efetivos contra o seu Inspermon!\n")

    if meu['tipo']=='Fogo':
        if Inspermons[oponente]['tipo']== 'Terra':
            meu['poder'] *= 1.6
        print("Os ataques de seu Inspermon vão ser super efetivos contra esse Inspermon tipo Terra!")
        if Inspermons[oponente]['tipo'] == 'Agua':
            Inspermons[oponente]['poder'] *=1.6
            print("\nCuidado! Os ataques desse oponente do tipo Agua serão super efetivos contra o seu Inspermon!\n")
    
    if meu['tipo']=='Ar':
        if Inspermons[oponente]['tipo'] == 'Agua':
            meu['poder'] *= 1.6
        print("\nOs ataques de seu Inspermon vão ser super efetivos contra esse Inspermon tipo Agua!\n")
        if Inspermons[oponente]['tipo'] == 'Terra':
            Inspermons[oponente]['poder'] *=1.6
            print("\nCuidado! Os ataques desse oponente do tipo Terra serão super efetivos contra o seu Inspermon!\n") 

    if meu['tipo']=='Terra':
        if Inspermons[oponente]["tipo"] == 'Ar':
            meu['poder'] *= 1.6
        print("\nOs ataques de seu Inspermon vão ser super efetivos contra esse Inspermon tipo Ar!\n")
        if Inspermons[oponente]['tipo'] == 'Fogo':
            Inspermons[oponente]['poder'] *=1.6
            print("\nCuidado! Os ataques desse oponente do tipo Fogo serão super efetivos contra o seu Inspermon!\n")

    while val:
        fuga = int(input('\nDeseja fugir da batalha? (1) Sim e (2) Não \n'))
        if fuga == 1:
            n = random.random()
            if n<=0.51:
                print('\nVocê fugiu da batalha!')
                val = False
            else:
                print('\nFuga sem sucesso!')
                e = 1
                while meu['vida'] > 0 and Inspermons[oponente]['vida']>0:
                    print(Fore.WHITE)
                    print('\n' + traço + '\n')
                    print(Fore.GREEN)
                    print("\nRound {0} :" .format(e))
                    time.sleep(0.8)
                    estringue = "\nO {0} possui {1} de vida  <----> O {2} possui {3} de vida..." .format(meu['nome'], meu['vida'], Inspermons[oponente]['nome'], Inspermons[oponente]['vida'])
                    funcao.escrita_timer(estringue)
                    e += 1
                    critical = random.random()
                    if critical >= 0.11:
                        Inspermons[oponente]['vida'] = Inspermons[oponente]['vida'] - meu['poder'] + Inspermons[oponente]['defesa']
                    else:
                        Inspermons[oponente]['vida'] = Inspermons[oponente]['vida'] - meu['poder']*1.1 + Inspermons[oponente]['defesa']
                        print("\nSeu Inspermon deu ataque crítico!!")
                    if Inspermons[oponente]['vida'] <= 0:
                        print("\nVocê derrotou seu oponente!")
                        print("\nA vida de seu Ipmon restante é: \n{0}".format(meu['vida']))
                        meu['xp'] +=10
                        val = False
                    else:
                        critical = random.random()
                        if critical >= 0.11:
                            meu['vida'] = meu['vida'] - Inspermons[oponente]['poder'] + meu['defesa']
                        elif critical < 0.11:
                            meu['vida'] = meu['vida'] - Inspermons[oponente]['poder']*1.1 + meu['defesa']
                            print("\nSeu Inspermon sofreu ataque crítico!!")

                        if meu['vida'] <= 0:
                            print("\nVocê foi derrotado!")
                            val = False
        elif fuga == 2:
            e=1
            while meu['vida'] > 0 and Inspermons[oponente]['vida']>0:
                print(Fore.WHITE)
                print('\n' + traço + '\n')
                print(Fore.GREEN)
                print("\nRound {0} :" .format(e))
                time.sleep(0.8)
                estringue = "\nO {0} possui {1} de vida  <----> O {2} possui {3} de vida" .format(meu['nome'], meu['vida'], Inspermons[oponente]['nome'], Inspermons[oponente]['vida'])
                funcao.escrita_timer(estringue)
                e += 1
                critical = random.random()
                if critical >= 0.11:
                    Inspermons[oponente]['vida'] = Inspermons[oponente]['vida'] - meu['poder'] + Inspermons[oponente]['defesa']
                else:
                    Inspermons[oponente]['vida'] = Inspermons[oponente]['vida'] - meu['poder']*1.8 + Inspermons[oponente]['defesa']
                    print("\nSeu Inspermon deu ataque crítico!!")
                if Inspermons[oponente]['vida'] <= 0:
                    print("\nVocê derrotou seu oponente!")
                    print("\nA vida de seu Ipmon restante é: \n{0}".format(meu['vida']))
                    meu["xp"] +=10
                    val = False
                else:
                    critical = random.random()
                    if critical >= 0.11:
                        meu['vida'] = meu['vida'] - Inspermons[oponente]['poder'] + meu['defesa']
                    elif critical < 0.11:
                        meu['vida'] = meu['vida'] - Inspermons[oponente]['poder']*1.8 + meu['defesa']
                        print("\nSeu Inspermon sofreu ataque crítico!!")

                    if meu['vida'] <= 0:
                        print("\nVocê foi derrotado!")
                        val = False
        else:
            print('\nVocê digitou o numero errado!')
