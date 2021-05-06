'''
Para passar na 2ª fase da olimpíada devem se cumprir pelo menos um dos seguintes requisitos:

- Total das notas superior a 25;
- Média superior a 8.

Complete as lacunas a seguir para que a solução fique de acordo com as regras acima.

'''

nota_portugues = 10
nota_ingles= 9
nota_literatura = 9

soma = nota_portugues + nota_ingles + nota_literatura
media = soma / 3

if media > 8 or soma > 25:
    print("Passou pra 2ª fase")
else:
    print("Desclassificado na 1ª Fase")