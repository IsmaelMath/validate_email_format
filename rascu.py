lista_provedores = {"hotmail", "gmail", "yahoo", "outlook"}
email = input("Informe o seu email principal: ")
for provedores in lista_provedores:

    if '@' in email:
        if provedores in email[email.index('@') + 1: email.index('.com')]:
            usuario = email[0: email.index('@')]
            provedor = email[email.index('@') + 1: email.index('.com')]
            print(f"Usuario: {usuario}")
            print(f"provedor: {provedor}")
            break
    else:
        print("O email informado esta incorreto, tente novamente.")