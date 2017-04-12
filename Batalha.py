import json, random, time
from colorama import Fore, Back, Style, init
from funções import função
init()

traço = "------"*18


def Batalha(meu,p,oponente,Inspermons):
    print(Fore.BLUE)
    print("Voce se deparou com um {0} selvagem!".format(Inspermons[oponente]['nome']))
    val = True
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
                    time.sleep(1)
                    estringue = "\nO {0} possui {1} de vida  <----> O {2} possui {3} de vida..." .format(meu['nome'], meu['vida'], Inspermons[oponente]['nome'], Inspermons[oponente]['vida'])
                    função.escrita_timer(estringue)
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
                time.sleep(1)
                estringue = "\nO {0} possui {1} de vida  <----> O {2} possui {3} de vida" .format(meu['nome'], meu['vida'], Inspermons[oponente]['nome'], Inspermons[oponente]['vida'])
                função.escrita_timer(estringue)
                e += 1
                critical = random.random()
                if critical >= 0.11:
                    Inspermons[oponente]['vida'] = Inspermons[oponente]['vida'] - meu['poder'] + Inspermons[oponente]['defesa']
                else:
                    Inspermons[oponente]['vida'] = Inspermons[oponente]['vida'] - meu['poder']*1.1 + Inspermons[oponente]['defesa']
                    print("\nSeu Insperom deu ataque crítico!!")
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
                        meu['vida'] = meu['vida'] - Inspermons[oponente]['poder']*1.1 + meu['defesa']
                        print("\nSeu Inspermon sofreu ataque crítico!!")

                    if meu['vida'] <= 0:
                        print("\nVocê foi derrotado!")
                        val = False
        else:
            print('\nVocê digitou o numero errado!')
