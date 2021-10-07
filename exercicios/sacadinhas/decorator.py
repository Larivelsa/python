# aprendendo como elaborar um decorator
# fonte: https://www.youtube.com/watch?v=r7Dtus7N4pI

# conceitos iniciais para compreender melhor o que é decorator

# função chamando outra função
def f1():
    print("Called f1")

def f2(f):
    f()

f2(f1)

# wrapper

def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")

    return wrapper

def f():
    print("Hello")

x = f1(f)
x()