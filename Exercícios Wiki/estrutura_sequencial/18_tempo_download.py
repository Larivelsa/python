'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) 
e a velocidade de um link de Internet (em Mbps), calcule e informe 
o tempo aproximado de download do arquivo usando este link (em minutos). 
'''

tamanho_arquivo_MB = float(input("Informe o tamanho do arquivo em MB: "))
velocidade_link_Mbps = float(input("Informe a velocidade do link em Mbps: "))

taxa_transferencia_Kbps = (velocidade_link_Mbps * 1024) / 8

tamanho_arquivo_KB = tamanho_arquivo_MB * 1024
tempo_download_segundos = tamanho_arquivo_KB / taxa_transferencia_Kbps
tempo_download_minutos = tempo_download_segundos / 60

if tempo_download_minutos < 1:
    print(f"O tempo de download será de {tempo_download_segundos:.2f} segundos")
else:
    print(f"O tempo de download será de {tempo_download_minutos:.2f} minutos")