import math
import minha_biblioteca

a = eval(input("Entre com o coeficiente a da equação: "))
b = eval(input("Entre com o coeficiente b da equação: "))
c = eval(input("Entre com o coeficiente c da equação: "))

delta = minha_biblioteca.calculaDelta(a, b, c)

print(f'O valor calculado do delta foi {delta}')

#delta > 0 : equação tem 2 raízes reais
#delta = 0: equação tem 1 raiz real
#delta < 0 : equação não tem raiz real
#raiz = (-b +- raiz_quadrada(delta))/2a

if delta>0:
    print("A equação tem 2 raízes reais.")
    raiz1 = (-b + math.sqrt(delta))/2*a
    raiz2 = (-b - math.sqrt(delta))/2*a
    print( f' As raizes da esquação são {raiz1} e {raiz2}')
elif delta == 0:
    print("A equação tem 1 raiz real.")
    raiz = (-b + math.sqrt(delta))/2*a
    print(f'A raiz da equação é {raiz}')
else: print("A equação não tem raiz real.")