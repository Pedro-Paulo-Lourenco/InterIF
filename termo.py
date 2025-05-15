while True:
    try:
        numero = int(input())
        x=[1,1,1,2,2]
        if numero <=5:
            print(x[numero-1])
        else:
            while len(x) < numero:
                x.append(x[len(x)-1]+x[len(x)-5])
            print(x[numero-1])
        
       # print(x)
    except EOFError:
        break