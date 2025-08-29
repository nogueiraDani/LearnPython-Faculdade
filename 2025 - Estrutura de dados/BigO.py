import random


def boo(dados):
    for i in dados:
        print(i)


# gerando 10 valores dentro de um intervalo de 0 até 9
dados = random.sample(range(10), 10)
boo(dados)


def boo2(dadosA, dadosB):
    for i in dadosA:
        print(i)
    for i in dadosB:
        print(i)


def boo3(dadosA, dadosB):
    for i in dadosA:
        for j in dadosB:
            print(i + j)


def boo4(dadosA, dadosB):
    for i in dadosA:
        for j in dadosB:
            print(i, j)


def boo5(dadosA, dadosB):
    for i in dadosA:
        for j in range(0, j < i * i, 1):
            print(i, j)


# Fatorial recursivo
def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        return n * fatorial(n-1)


# programa princinpal
x = fatorial(5)
print(x)


# Fibonacci recursivo
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# programa princinpal
x = fib(5)
print(x)


# Exercício 1
def Exercicio1(dados):
    for i in range(0, len(dados)/2, 1):
        dados[i] = i * 2



# Exercício 2
def Exercicio2(dados):
    for i in range(0, len(dados), 1):
        dados[i] = i + 1
    for i in range(0, len(dados), 1):
        dados[i] = i - 1


# Exercício 3
def Exercicio3(dados):
    for i in range(0, len(dados), 1):
        for j in range(0, len(dados), 1):
            dados[i] = dados[j] + 1


# Exercício 4
def Exercicio4(dados):
    for i in range(0, len(dados), 1):
        for j in range(0, len(dados), 1):
            for k in range(0, 9000000, 1):
                dados[i] = dados[j] + 1
