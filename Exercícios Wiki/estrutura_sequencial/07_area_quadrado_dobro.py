# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Informe a medida do lado do quadrado: "))

area_dobro = (lado ** 2)*2

print(
    f"O dobro da medida do quadrado com o lado informado é de {area_dobro:.2f}")
