'''
Complete o código a seguir para que esteja de acordo com os itens:

- A lista que contém os números ímpares deve se chamar "impares";
- A lista que contém os números pares deve se chamar "pares".
- Deve ser criada uma variável chamada "numero_1" que deve receber o menor valor da lista de números ímpares;
- Deve ser criada uma variável chamada "numero_2" que deve receber o maior valor dos números pares;
- Por fim. deve ser criada uma variável com o nome "soma", que deve receber o somatório das variáveis criadas.

'''

impares = [1, 3, 5, 7, 9]
pares = [2, 4, 6, 8, 10]

numero_1 = min(impares)
numero_2 = max(pares)

soma = numero_1+numero_2

print("A soma entre o menor número ímpar e o maior número par é: " + str(soma))