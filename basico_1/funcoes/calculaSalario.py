#Calculadora de salário

def calcular_pagamento(qtd_horas, valor_hora):
  horas = float(qtd_horas)
  taxa = float(valor_hora)
  if horas <= 40:
    salario=horas*taxa
  else:
    h_excd = horas - 40
    salario = 40*taxa+(h_excd*(1.5*taxa))
  return salario

qtd_horas = input('Digite a quantidade de horas: ')
valor_hora = input('Digite o valor da hora: ')
print('Valor do salário a ser recebido na semana: ',calcular_pagamento(qtd_horas, valor_hora))