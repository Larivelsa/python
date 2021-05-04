'''
No código abaixo temos uma função que retorna a soma dos valores de uma coleção. Preencha as lacunas seguindo os seguintes requisitos:

- o nome da função deve ser "retorna_soma";
- a função "retorna_soma" deve receber um parâmetro chamado "valores";
- a variável "soma" deve ser usada no loop for para depois retornar a soma dos elementos da coleção;
- use a variável "soma_numeros" para receber o retorno da função "retorna_soma".
'''

def retorna_soma(valores):
    soma = 0
    for valor in valores:
        soma = soma + valor
    return soma

numeros = [5, 10, 15, 25]
soma_numeros = retorna_soma(numeros)
print(soma_numeros)