'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% 
    
Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

            Salário Bruto: (5 * 220)        : R$ 1100,00
            (-) IR (5%)                     : R$   55,00  
            (-) INSS ( 10%)                 : R$  110,00
            FGTS (11%)                      : R$  121,00
            Total de descontos              : R$  165,00
            Salário Liquido                 : R$  935,00
'''
valor_hora = float(input("Informe o valor da hora trabalhada: "))
quantidade_hora = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * quantidade_hora

if salario_bruto <= 900:
    taxa_ir = 0
    calculo_imposto_renda = 0
    calculo_inss = salario_bruto * 0.08
    calculo_fgts = salario_bruto * 0.11 #não desconta do salário
    calculo_sindicato = salario_bruto * 0.03
    descontos = calculo_imposto_renda + calculo_inss + calculo_sindicato

elif salario_bruto <= 1500:
    taxa_ir = 0.05
    calculo_imposto_renda = salario_bruto * taxa_ir
    calculo_inss = salario_bruto * 0.08
    calculo_fgts = salario_bruto * 0.11 #não desconta do salário
    calculo_sindicato = salario_bruto * 0.03
    descontos = calculo_imposto_renda + calculo_inss + calculo_sindicato

elif salario_bruto <= 2500:
    taxa_ir = 0.1
    calculo_imposto_renda = salario_bruto * taxa_ir
    calculo_inss = salario_bruto * 0.08
    calculo_fgts = salario_bruto * 0.11 #não desconta do salário
    calculo_sindicato = salario_bruto * 0.03
    descontos = calculo_imposto_renda + calculo_inss + calculo_sindicato

else:
    taxa_ir = 0.2
    calculo_imposto_renda = salario_bruto * taxa_ir
    calculo_inss = salario_bruto * 0.08
    calculo_fgts = salario_bruto * 0.11 #não desconta do salário
    calculo_sindicato = salario_bruto * 0.03
    descontos = calculo_imposto_renda + calculo_inss + calculo_sindicato

salario_liquido = salario_bruto - descontos 

print(f'''
    + Salário Bruto : R$ {salario_bruto:.2f}
    - IR ({taxa_ir*100:.0f} %) : R$ {calculo_imposto_renda:.2f}
    - INSS (8 %) : R$ {calculo_inss:.2f}
    - Sindicato (5 %) : R$ {calculo_sindicato:.2f}
      FGTS (11 %) : R$ {calculo_fgts:.2f}
    = Salário Liquido : R$ {salario_liquido:.2f}
''')