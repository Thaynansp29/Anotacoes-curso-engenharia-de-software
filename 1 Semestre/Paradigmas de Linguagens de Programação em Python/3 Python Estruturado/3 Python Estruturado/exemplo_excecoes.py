numerador = eval(input("Entre com o numerador da fração: "))
denominador = eval(input("Entre com o denominador da fração: "))

try:
    print(f'A divisão vale {numerador/denominador}')
except ZeroDivisionError:
    print("Os parâmetros informados são inválidos - Divisão por zero")
except:
    print("Não foi possível executar a operação")

