generator = (i ** 2 for i in range(11) if i % 2 == 0)
# gera sob demanda
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator)) # gera erro a partir desta linha qp passa do range