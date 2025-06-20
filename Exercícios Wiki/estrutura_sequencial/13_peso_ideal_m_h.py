# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

sexo = input("Informe seu sexo (m para mulher h para homem): ")
altura = float(input("Informe a sua altura em metros: "))

peso_ideal = (72.2 * altura) - 58

if sexo.lower() == 'm':
    peso_ideal = (62.1*altura) - 44
elif sexo.lower() == 'h':
    peso_ideal = (72.7 * altura) - 58
else:
    print("Caractere inválido!")


print(f"Seu peso ideal é de {peso_ideal:.2f}")
