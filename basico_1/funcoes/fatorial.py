'''
Qual das alternativas a seguir tem uma função que atende aos seguintes requisitos:

- Uma função que tenha o nome "fatorial";
- Essa função deve retornar um valor;
- A função deve receber um número para calcular seu fatorial.

'''

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

valor_fatorial = fatorial(5)

print(valor_fatorial)