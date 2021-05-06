'''
O código a seguir pede para que uma idade seja informada, retornando uma descrição 
de acordo com o valor informado.

Complete as lacunas vazias para que o código funcione de acordo com os itens listados:

- criança/bebê -> menos de 13 anos;
- adolescente -> entre 13 e 17 anos;
- jovem -> entre 18 e 29 anos;
- adulto -> entre 30 e 100 anos.
'''

idade = int(input('Digite sua idade: ')) # Informando a idade

if idade < 13:
    print('Você é criança ou bebê')
elif idade >= 13 and idade < 18:
    print('Você é adolescente')
elif idade >=18 and idade < 30:
    print('Você é jovem')
elif idade >= 30 and idade <= 100:
    print('Você é adulto')
else:
    print('Valor não encontrado!')