# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Informe o valor da hora trabalhada: "))
horas_trabalhadas_mes = float(
    input("Informe o número de horas trabalhadas no mês: "))
salario = valor_hora * horas_trabalhadas_mes

print(f"O salário é de {salario}")
