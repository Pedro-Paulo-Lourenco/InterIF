preco_pacotinho = int(float(input()[2:])*100)
valores_moedas = [25, 10, 5, 1]

quantidade_moedas = [int(i) for i in input().split(" ")]

total_dinheiro = sum([valores_moedas[i] * quantidade_moedas[i] for i in range(4)])

pacotes_comprados = total_dinheiro//preco_pacotinho

conta = preco_pacotinho * pacotes_comprados

for i in range(4):
    while conta >= valores_moedas[i] and quantidade_moedas[i] > 0:
        conta -= valores_moedas[i]
        quantidade_moedas[i] -= 1

print(pacotes_comprados)
print(sum(quantidade_moedas))