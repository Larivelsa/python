def quadrado(x):
    return x**2

def soma_quadrado(a,b,c):
    a = quadrado(a)
    b = quadrado(b)
    c = quadrado(c)
    return a+b+c

z = soma_quadrado(1,2,3)
print(z)