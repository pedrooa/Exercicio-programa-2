#Ep02 - Inspermon
import random
import json

#Mostrar os tres pokemons iniciais em ordem numero de 0-2, para depois o usuario escolher qual deseja
def inspermon_inicial(ipmon_inicial):
    meu = ipmon_inicial
    return meu

def mostra_inspermon(ipmon):
    print('Inspermon : {0}'. format(ipmon['nome']))
    print('Poder = {0}'. format(ipmon['poder']))
    print('Defersa = {0}'. format(ipmon['defesa']))
    print('Vida =  {0} \n'. format(ipmon['vida']))


with open('inspermons.json') as arquivo:
    inspermons = json.load(arquivo)
#for ipmon in inspermons:
    #mostra_inspermon(ipmon)

while True:
    açao_usuario = input('Você pode andar e procurar Inspermons ou dormir para recuperar sua vida. \n Digite 1 para andar ou 0 para dormir: ')
    if açao_usuario == 0:
        print('Dormindo')
    elif açao_usuario == 1:
        print('Andando')
    print('Qual pokemon deseja usar: \n Charmander (0) \n Squirtle (1) \n Bulbasaur(2) \n')
    print(inspermon_inicial(ipmon))
    ipmon_inicial_var = input('Digite o numero do pokemon (0 - 2): ')
