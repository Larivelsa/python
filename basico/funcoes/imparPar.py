'''
Complete a função abaixo para que verifique se um número informado é par ou ímpar. 
Siga os itens a seguir para preencher as lacunas:

- O nome da função deve ser "verifica_numero" e ela deve ter um parâmetro chamado "num";
- A variável que vai receber o dado digitado pelo usuário deve se chamar "numero";
- Na última lacuna, a função "verifica_numero" deve ser chamada. (Use a variável criada).
'''


def verifica_numero(num):

    if num % 2 == 0:
        print("Esse número é par!")
    else:
        print("Esse número é ímpar")


numero = int(input("Digite um número: "))

verifica_numero(numero)
