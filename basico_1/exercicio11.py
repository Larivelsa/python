'''
O código abaixo deve atender aos seguintes itens:

- Deve uma função com o nome "soma" que apenas retorna a soma entre dois números;
- O 1º parâmetro da função "soma" deve se chamar "num_1". O 2º parâmetro deve se chamar "num_2";
- Os valores dos números devem ser digitados pelo usuário;
- A variável "soma_numeros" deve receber o retorno da função;
- No final, deve ser impresso o valor de "soma_numeros".

'''

def soma(num_1,num_2):
  return num_1+num_2 

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

soma_numeros = soma(numero_1,numero_2)
print(soma_numeros)



