import func

capital_inicial = int(input("Informe o capital incial: "))
juros = float(input("informe o juros ao ano: "))
tempo = int(input("Informe o tempo que o capital ficara alocado: "))
x = input("Informe a operaçao que deseja executar se e js ou jc: ")

while True:
    if x.lower() == "js" or x.lower() == "jc":
        func.calcular(x, capital_inicial, juros, tempo)
        break
    else:
        print("essa opeçao nao existe. Tente novamente.")
