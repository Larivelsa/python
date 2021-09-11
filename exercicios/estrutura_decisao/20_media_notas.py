'''
Faça um Programa para leitura de três notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e presentar:

    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10. 
'''

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
n3 = float(input('Informe a terceira nota: '))
media = (n1 + n2 + n3) / 3

if media < 7:
    mensagem = f'Reprovado. Média {media:.2f}'
elif 10 > media >= 7:
    mensagem = f'Aprovado. Nota {media:.2f}'
else:
    mensagem = f'Aprovado com distinção! Nota {media:.2f}'

print(mensagem)
