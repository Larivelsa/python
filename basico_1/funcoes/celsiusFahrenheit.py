'''
Abaixo temos uma função que converte a temperatura de Celsius para Fahrenheit.
 Preencha as lacunas para que o código funcione de acordo com os itens abaixo:

- o nome da função deve ser "celsius_fahrenheit";
- a função "celsius_fahrenheit" deve possuir a seguinte fórmula:

Temperatura Fahrenheit = (Temperatura Celsius * 9 / 5 ) + 32
(use essa mesma ordem da fórmula no código)

'''

temperatura_celsius = int(input("Digite a temperatura em graus celsius: "))

def celsius_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius*9/5)+32
    return temp_fahrenheit

temperatura_fahrenheit = celsius_fahrenheit(temperatura_celsius)

print(temperatura_celsius,"°C equivalem a : ", temperatura_fahrenheit, "°F")