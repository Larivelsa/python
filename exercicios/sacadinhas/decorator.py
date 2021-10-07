# aprendendo como elaborar um decorator
# fonte: https://www.youtube.com/watch?v=r7Dtus7N4pI

# conceitos iniciais para compreender melhor o que é decorator

# função chamando outra função
def f1():
    print("Called f1")

def f2(f):
    f()

f2(f1)

# wrapper e decorator

def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")

    return wrapper

@f1 
# @f1 é o mesmo que se fizermos x = f1(f)
def f():
    print("Hello")

f()

# por questões de receber parâmetros diversos, ver conceitos de *args, **kwargs


