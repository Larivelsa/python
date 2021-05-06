'''.
Para conquistar um prêmio é necessário satisfazer pelo menos uma das condições abaixo:

- Fazer mais de 120 pontos;
- Conquistar no mínimo 13 desafios.

Complete o código a seguir para que ele atenda as regras descritas acima.

'''

premio = False

pontos = 110
desafios = 15

if pontos > 120 or desafios >= 13:
    premio = True

print(premio)