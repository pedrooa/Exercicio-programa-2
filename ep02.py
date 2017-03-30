#Ep02 - Inspermon
import random
import json
from Batalha import Batalha
InsperDex = []
#Mostrar os tres pokemons iniciais em ordem numero de 0-2, para depois o usuario escolher qual deseja
def inspermon_inicial(ipmon_inicial):
    return Inspermons[ipmon_inicial]

def mostra_inspermon(p):
    print('Inspermon : {0}'. format(Inspermons[p]['nome']))
    print('Poder = {0}'. format(Inspermons[p]['poder']))
    print('Defersa = {0}'. format(Inspermons[p]['defesa']))
    print('Vida =  {0} \n'. format(Inspermons[p]['vida']))


with open('inspermons.json') as arquivo:
    Inspermons = json.load(arquivo)
#for ipmon in inspermons:
    #mostra_inspermon(ipmon)

while True:
    açao_usuario = int(input('Você pode andar e procurar Inspermons ou dormir para recuperar sua vida. \n Digite 1 para andar ou 0 para dormir: '))
    if açao_usuario == 0:
        print('Dormindo')
        break#O jogo acaba quando o jogador vai dormir
    elif açao_usuario == 1:
        print('Andando')
        p = int(input('Qual pokemon deseja usar: \n Charmander (0) \n Squirtle (1) \n Bulbasaur(2) \n'))#obs: funciona com outros pokemons se o jogador escolher numeros acima de 2
        meu = inspermon_inicial(p)
        print("Stats iniciais de seu Ipmons: {0}".format(meu))
        oponente = random.randrange(len(Inspermons))
        perdeu = False
        Batalha(meu,p, oponente)
        if perdeu == True:
            print('seu Inspermon esta inconsciente, va a helpdesk imediatamente recuperar a vida dele!')
            break



        












