entrada = int(input())

def funcao(x):
    if x >= 10000000:
        x-=3
    elif x < 10000000:
        funcao(funcao(funcao(x+13)))
    return x

print(funcao(entrada))