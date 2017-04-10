#Ep02 - Inspermon
import random, json
from funções import função
from colorama import Fore, Back, Style
from Batalha import Batalha

with open('inspermons.json') as arquivo:
    Inspermons = json.load(arquivo)

Insperdex = []
#Cria a lista com os ipmon iniciais e cria uma lista com os valores padrão de vida
meus_ipmon = função.lista_meus_ipmons(Inspermons)
vidas = []
traço = "------"*15

#Cria lista de vidas iniciais
for e in meus_ipmon:
    vidas.append(e["vida"])

Checkpoint = [meus_ipmon]  #Prevenção de erros caso o jogador tente dar Save sem ter jogado nada.

load = int(input('\nDeseja carregar um jogo existente?\n1   -   Sim\n2   -   Nao\n'))
while True:
    if load == 1:
        with open('SaveGame.json','r') as arquivo:
            dados = json.load(arquivo)
        meus_ipmon = dados[0]
        Insperdex = dados[1]
        vidas = dados[2]
        break
    elif load == 2:
        break
    else:
        print('Codigo Inexistente!')

while True:
    print('\n' + traço + '\n')
    açao_usuario = int(input('\nVocê pode andar e procurar Inspermons ou dormir para recuperar sua vida. \nDigite 1 para andar ou 2 para dormir: '))
    if açao_usuario == 2:
        #Pergunta ao usuário se quer salvar o jogo
        print('\n' + traço + '\n')
        save = int(input('\nDeseja salvar seu progresso?(Obs : Isso vai deletar seu save passado)\n1   -   Sim\n2   -   Nao\n'))
        if save == 1:
            with open('SaveGame.json','w') as arquivo:
                json.dump(Checkpoint,arquivo)
            print('\n' + traço + '\n')
            print('\nJogo salvo com sucesso!\nDormindo!')
            break
        elif save ==2:
            print('\n' + traço + '\n')
            print('\n Dormindo!')
            break
        else:
            print('Codigo inexistente!')
    elif açao_usuario == 1:
        #Pergunta ao usuário qual inspermon ele quer usar
        p = função.inspermon_usuario(meus_ipmon)
        if meus_ipmon[p]['vida'] == 0:
            print('\nSeu InsperMon possui zero de vida!')
            string = "\nCurando ...\n"
            função.escrita_timer(string)
            print('InsperMon Curado!')
            meus_ipmon[p]['vida'] = vida


        #Armazena a vida inicial do ipmon
        vida = vidas[p]
        #Separa com traços
        print('\n' + traço + '\n')
        #Roda a função timer para a string
        string = "\nAndando ...\n"
        função.escrita_timer(string)
        #Adiciona os Inspermons ao Insperdex
        if meus_ipmon[p]['nome'] not in Insperdex:
            Insperdex.append(meus_ipmon[p]['nome'])
        #Gera o pokemon aleatório para combate
        oponente = random.randrange(len(Inspermons))
        if Inspermons[oponente]['nome'] not in Insperdex:
            Insperdex.append(Inspermons[oponente]['nome'])
        print('\n' + traço + '\n')
        print("\nStats iniciais de seu InsperMon: \nInspermon : {0}\nPoder = {1}\nVida = {2}\nDefesa = {3}\nXp = {4}".format(meus_ipmon[p]['nome'],meus_ipmon[p]['poder'],meus_ipmon[p]['vida'],meus_ipmon[p]['defesa'],meus_ipmon[p]['xp']))
        #Batalha entre os Inspermons
        Batalha(meus_ipmon[p],p, oponente,Inspermons)
        #Corrige a vida do Inspermon
        função.correcao_vida(meus_ipmon, p)
        while True:
            print('\n' + traço + '\n')
            hp = int(input("\nBem Vindo ao helpdesk! Digite (1) para recuperar a vida de seu Inspermon, ou (2) para continuar: "))
            #Condições para recuperação de vida
            if hp == 1:
                meus_ipmon[p]['vida'] = vida
                break
            elif hp == 2:
                break
            else:
                print('\n' + traço + '\n')
                print('\nEscreva direito!')
        #Condição para evolução do Inspermon
        if meus_ipmon[p]["xp"] >= 50:
            print('\n' + traço + '\n')
            print("\nSeu InsperMon está evoluindo!")
            meus_ipmon[p]["xp"] = 0
            meus_ipmon[p]["poder"] +=15
            vidas[p] += 100
            meus_ipmon[p]["vida"] = vidas[p]
            meus_ipmon[p]["defesa"] +=5
        #Mostra o Insperdex
        print('\n' + traço + '\n')
        print('\nSeu Insperdex é:')
        função.mostra_insperdex(Insperdex)
        #Salva meusipmon, insperdex e referencia dos valores de vida
        Checkpoint = [meus_ipmon,Insperdex,vidas]
    else:
        print("\nCódigo incorreto, redigite!")
