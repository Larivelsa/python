'''
Abaixo temos os pesos de Lucas, Darlan, Miguel e Caio.
Complete o código abaixo para verificar se a soma dos pesos dos 4 amigos é permitida no elevador.

OBS: Defina a condição de acordo com as mensagens.

'''
peso_lucas = 90.7
peso_darlan = 88.4
peso_miguel = 97.3
peso_caio = 102.9

soma_pesos = peso_lucas + peso_miguel + peso_caio

capacidade_elevador = 250
if soma_pesos >= capacidade_elevador:
    print("Os 4 amigos não podem ir juntos no elevador :(")
else:
    print("Os 4 amigos podem ir no elevador de uma vez :)")