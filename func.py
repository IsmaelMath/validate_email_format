
def js(capital_inicial, juros, tempo):
    montante = capital_inicial + capital_inicial * (juros / 100) * tempo
    print(f"O capital no estante t{tempo}: R$ {montante: .2f}")
    return montante


def jc(capital_inicial, juros, tempo):
    montante = capital_inicial * (1 + juros / 100) ** tempo
    print(f"O capital no estante t{tempo}: R$ {montante: .2f}")
    return montante


def calcular(x, capital_inicial, juros, tempo):
    if x.lower() == "js":
        js(capital_inicial, juros, tempo)
    else:
        jc(capital_inicial, juros, tempo)
        
