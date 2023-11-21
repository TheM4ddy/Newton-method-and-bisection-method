# Bethany Sylvatica Valentine BV3026027


#Definicao da funcao de newton
def newton(erro_valor):
    #definicao de contar
    count = 0
    x = 1
    while True:
        #definicao da funcao
        x1 = x - ( ( x**3 - 7 * x**2 + 14 * x - 6) / (3 * x**2 - 14 * x + 14) )
        count += 1
        if (abs(x1-x)/ abs(x1)) < erro_valor:
            break
        x = x1
    return x1,count

#definicao da funcao de bisseccao
def bissec(erro_valor):
    iteracoes = 0
    a = 0
    a1 = 1
    temp = 0
    while True:
        #definicao da funcao
        a2 = (a + a1) / 2
        iteracoes += 1
        fa = (a**3) - (7 * (a**2)) + (14 * a) - 6
        fa1 = (a1**3) - (7 * (a1**2)) + (14 * a1) - 6
        fa2 = (a2**3) - (7 * (a2**2)) + (14 * a2) - 6
        if(fa < 0 ):
            temp = a1
            a1 = a
            a = temp
            temp = fa1
            fa1 = fa
            fa = temp
        if(fa2 > 0 and fa2 < fa):
            a = a2
        elif(fa2 < 0 and fa2 > fa1):
            a1 = a2
        if (abs(a1-a)/ abs(a1)) < erro_valor:
            break
    return a2,iteracoes

def main():
    print("Feito por Bethany com ajuda de Luis Zucata...")
    erro = input("Digite a precisão da resposta: 10^")
    erro_valor = float(10**float(erro))
    x1, count = newton(erro_valor)
    print("+--------+")
    print("| Newton |")
    print("+--------+")
    print("=> Quantidade de iteracoes: " + str(count) +
          "\n=> Resultado do Newton: " + str(x1))
    a2, iteracoes = bissec(erro_valor)
    print("+-----------+")
    print("| Bisseccao |")
    print("+-----------+")
    print("=> Quantidade de iteracoes: " + str(iteracoes) +
          "\n=> Resultado do Bisseccao: " + str(a2))
main()
