#Imprime lista_programadores em maiúsculo

lista_programadores = ['Larissa', 'Mateus', 'Jesus', 'Luciana', 'Juliana', 'Guilherme']

def imprime_maiusculo(programadores):
  for programador in programadores: 
    print(programador.upper())

imprime_maiusculo(lista_programadores)