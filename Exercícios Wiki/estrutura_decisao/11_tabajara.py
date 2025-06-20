'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa 
que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''
salario_antigo = int(input("Informe o salário: "))

if salario_antigo <= 280:
    salario_novo = salario_antigo * 1.2
    percentual = 20
elif salario_antigo < 700:
    salario_novo = salario_antigo * 1.15
    percentual = 15
elif salario_antigo < 1500:
    salario_novo = salario_antigo * 1.1
    percentual = 10
else:
    salario_novo = salario_antigo * 1.05
    percentual = 5

print(f'Salário antes do reajuste: R$ {salario_antigo:.2f} - Valor do aumento: R$ {(salario_novo-salario_antigo):.2f} - Salário novo: R$ {salario_novo:.2f} - Percentual de aumento usado: {percentual}%')