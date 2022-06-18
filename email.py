lista_provedores = ["hotmail", "gmail", "outlook", "yahoo"]

while True:
    email = input("Informe seu e-mail: ")

    if "@" in email and email[email.index("@")+1: email.index(".com")] in  lista_provedores:
        usuario = email[0: email.index("@")]
        provedor = email[email.index("@")+1: email.index(".com")]
        print("O usuário do e-mail é: ", usuario)
        print("O provedor do e-mail é: ", provedor)
        break
    else:
        print(f"O formato de e-mail não existe : {email} .... Tente novamente!!")
