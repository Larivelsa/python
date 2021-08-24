'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% 
para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido. 
    '''

valor_hora = float(input("Informe o valor da hora trabalhada: "))
quantidade_hora = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * quantidade_hora
calculo_inss = salario_bruto * 0.08
calculo_imposto_renda = salario_bruto * 0.11
calculo_sindicato = salario_bruto * 0.05
descontos = calculo_inss + calculo_imposto_renda + calculo_sindicato

salario_liquido = salario_bruto - descontos 

print(f'''
    + Salário Bruto : R$ {salario_bruto}
    - IR (11%) : R$ {calculo_imposto_renda}
    - INSS (8%) : R$ {calculo_inss}
    - Sindicato ( 5%) : R$ {calculo_sindicato}
    = Salário Liquido : R$ {salario_liquido}
''')