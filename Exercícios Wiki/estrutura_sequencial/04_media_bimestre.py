# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))
n4 = float(input("Informe a quarta e última nota: "))

media = (n1+n2+n3+n4)/4

print(f"A média do bimestre é {media:.2f}")
