'''
Complete o código abaixo de modo que atenda aos seguintes requisitos:

- Deve ser criada uma função com o nome "calcula_desconto", que deve receber os seguintes parâmetros:
- 1º parâmetro: deve ter o nome "preco" (representa o valor do produto);
- 2º parâmetro: deve ter o nome "desconto" (representa o percentual de desconto a ser aplicado no preço);
- No final devem ser impressos os valores do produto sem desconto e com desconto;
'''

def calcula_desconto(preco,desconto):
    novo_preco = preco - ( preco * desconto )
    return novo_preco

preco = 50
desconto = 0.1

preco_com_desconto = calcula_desconto(preco,desconto)

print("O preço do produto é: ", preco)
print("O preço do produto com desconto é: ",  preco_com_desconto)