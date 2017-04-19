#Ep02 - Inspermon
import random, json
import colorama
from funcoes import funcao
from colorama import Fore, Back, Style, init
from Batalha import Batalha
init()

with open('inspermons.json') as arquivo:
    Inspermons = json.load(arquivo)

Insperdex_nome = []
Insperdex = []
#Cria a lista com os ipmon iniciais e cria uma lista com os valores padrão de vida
meus_ipmon = funcao.lista_meus_ipmons(Inspermons)
vidas = []
traço = "------"*15


#Cria lista de vidas iniciais
for e in meus_ipmon:
    vidas.append(e["vida"])

Checkpoint = [meus_ipmon]  #Prevenção de erros caso o jogador tente dar Save sem ter jogado nada.
print(Fore.RED)
load = int(input('\nDeseja carregar um jogo existente?\n1   -   Sim\n2   -   Nao\n'))
while True:
    if load == 1:
        with open('SaveGame.json','r') as arquivo:
            dados = json.load(arquivo)
        meus_ipmon = dados[0]
        Insperdex = dados[1]
        vidas = dados[2]
        Insperdex_nome = dados[3]
        break
    elif load == 2:
        break
    else:
        print('Codigo Inexistente!')

while True:
    print(Fore.WHITE)
    print('\n' + traço + '\n')
    print(Fore.YELLOW)
    açao_usuario = int(input('\nVocê pode caçar outros pokemons, dormir ou abrir o Insperdex.\nDigite: \n(1) para andar\n(2) para dormir\n(3) para abrir o Insperdex\n : '))
    if açao_usuario == 2:
        #Pergunta ao usuário se quer salvar o jogo
        print(Fore.WHITE)
        print('\n' + traço + '\n')
        print(Fore.BLUE)
        save = int(input('\nDeseja salvar seu progresso?(Obs : Isso vai deletar seu save passado)\n1   -   Sim\n2   -   Nao\n'))
        if save == 1:
            with open('SaveGame.json','w') as arquivo:
                json.dump(Checkpoint,arquivo)
            print(Fore.WHITE)
            print('\n' + traço + '\n')
            print(Fore.BLUE + '\nJogo salvo com sucesso!\nDormindo!')
            break
        elif save ==2:
            print(Fore.WHITE)
            print('\n' + traço + '\n')
            print(Fore.BLUE + '\n Dormindo!')
            break
        else:
            print(Fore.BLUE + 'Codigo inexistente!')
    elif açao_usuario == 1:
        #Pergunta ao usuário qual inspermon ele quer usar
        p = funcao.inspermon_usuario(meus_ipmon)
        if meus_ipmon[p]['vida'] == 0:
            print(Fore.GREEN + '\nSeu InsperMon possui zero de vida!')
            string = "\nCurando ...\n"
            funcao.escrita_timer(string)
            print('InsperMon Curado!')
            meus_ipmon[p]['vida'] = vida

        #Armazena a vida inicial do ipmon
        vida = vidas[p]
        #Separa com traços
        print(Fore.WHITE)
        print('\n' + traço + '\n')
        print(Fore.GREEN)
        #Roda a funcao timer para a string
        string = "\nAndando ...\n"
        print(Fore.BLUE)
        funcao.escrita_timer(string)
        #Adiciona os Inspermons ao Insperdex
        if meus_ipmon[p]['nome'] not in Insperdex_nome:
            Insperdex_nome.append(meus_ipmon[p]['nome'])
            Insperdex.append(meus_ipmon[p])
        #Gera o pokemon aleatório para combate
        oponente = random.randrange(len(Inspermons))
        if Inspermons[oponente]['nome'] not in Insperdex_nome:
            Insperdex_nome.append(Inspermons[oponente]['nome'])
            Insperdex.append(Inspermons[oponente])
        print(Fore.WHITE)
        print('\n' + traço + '\n')
        print(Fore.GREEN)
        print("\nStats iniciais de seu InsperMon: \nInspermon : {0}\nPoder = {1}\nVida = {2}\nDefesa = {3}\nTipo = {4}\nXp = {5}".format(meus_ipmon[p]['nome'],meus_ipmon[p]['poder'],meus_ipmon[p]['vida'],meus_ipmon[p]['defesa'],meus_ipmon[p]['tipo'],meus_ipmon[p]["xp"]))
        #Batalha entre os Inspermons
        Batalha(meus_ipmon[p],p, oponente,Inspermons)
        #Corrige a vida do Inspermon
        funcao.correcao_vida(meus_ipmon, p)
        while True:
            print(Fore.WHITE)
            print('\n' + traço + '\n')
            print(Fore.BLUE)
            hp = int(input("\nBem Vindo ao helpdesk! Digite (1) para recuperar a vida de seu Inspermon, ou (2) para continuar: "))
            #Condições para recuperação de vida
            if hp == 1:
                meus_ipmon[p]['vida'] = vida
                break
            elif hp == 2:
                break
            else:
                print(Fore.WHITE)
                print('\n' + traço + '\n')
                print(Fore.BLUE)
                print('\nEscreva direito!')
        #Condição para evolução do Inspermon
        if meus_ipmon[p]["xp"] >= 50:
            print(Fore.WHITE)
            print('\n' + traço + '\n')
            print(Fore.RED)
            estringue ="\nSeu InsperMon está evoluindo!"
            funcao.escrita_timer(estringue)
            meus_ipmon[p]["xp"] = 0
            meus_ipmon[p]["poder"] +=25
            vidas[p] += 150
            meus_ipmon[p]["vida"] = vidas[p]
            meus_ipmon[p]["defesa"] +=5
        #Salva meusipmon, insperdex e referencia dos valores de vida
        Checkpoint = [meus_ipmon,Insperdex,vidas,Insperdex_nome]
    elif açao_usuario == 3:
        print(Fore.WHITE)
        print('\n' + traço + '\n')
        print(Fore.YELLOW)
        print('\nSeu Insperdex é:')
        funcao.mostra_insperdex(Insperdex)
    else:
        print("\nCódigo incorreto, redigite!")
