qtd_pedacos = int(input())
precos = [float(i) for i in input().split(" ")]

valor_bolo = 0
fatias_compradas = 0

#while qtd_pedacos > fatias_compradas:
for pedacos in range(qtd_pedacos):
    for otropedaco in range(qtd_pedacos):
        if fatias_compradas == qtd_pedacos:
            break
        elif precos[pedacos]/(pedacos+1) <= precos[otropedaco]/(otropedaco+1):
            valor_bolo += precos[pedacos]
            fatias_compradas += pedacos+1
            

print("{:.2f}".format(valor_bolo))
