pacote = float(input("Informe o valor bruto do pacote R$: "))
assento = (input("Informe a categoria do assento: "))
pessoa = int(input("Informe a quantidade de viajantes: "))

if assento.upper() == "ECONOMICA" or assento.upper() == "ECONÔMICA":
    if pessoa == 2:
        desconto = float(pacote * 0.03)
        liquido = float(pacote - desconto)
        print("O pacote de {}R$, para 2 pessoas tem desconto de: {}R$".format(pacote,desconto))
        print("Valor liquido: {} R$".format(liquido))
    elif pessoa == 3:
        desconto = float(pacote * 0.04)
        liquido = float(pacote - desconto)
        print("O pacote de {}R$, para 2 pessoas tem desconto de: {}R$".format(pacote,desconto))
        print("Valor liquido: {} R$".format(liquido))
    elif pessoa >= 4:
        desconto = float(pacote * 0.05)
        liquido = float(pacote - desconto)
        print("O pacote de {}R$, para 2 pessoas tem desconto de: {}R$".format(pacote,desconto))
        print("Valor liquido: {} R$".format(liquido))

elif assento.upper() == "EXECUTIVA":
    if pessoa == 2:
        desconto = float(pacote * 0.05)
        liquido = float(pacote - desconto)
        print("O pacote de {}R$, para 2 pessoas tem desconto de: {}R$".format(pacote,desconto))
        print("Valor liquido: {} R$".format(liquido))
    elif pessoa == 3:
        desconto = float(pacote * 0.07)
        liquido = float(pacote - desconto)
        print("O pacote de {}R$, para 2 pessoas tem desconto de: {}R$".format(pacote,desconto))
        print("Valor liquido: {} R$".format(liquido))
    elif pessoa >= 4:
        desconto = float(pacote * 0.08)
        liquido = float(pacote - desconto)
        print("O pacote de {}R$, para 2 pessoas tem desconto de: {}R$".format(pacote,desconto))
        print("Valor liquido: {} R$".format(liquido))

elif assento.upper() == "PRIMEIRA CLASSE" or assento.upper() == "PRIMEIRACLASSE":
    if pessoa == 2:
        desconto = float(pacote * 0.10)
        liquido = float(pacote - desconto)
        print("O pacote de {}R$, para 2 pessoas tem desconto de: {}R$".format(pacote,desconto))
        print("Valor liquido: {} R$".format(liquido))
    elif pessoa == 3:
        desconto = float(pacote * 0.15)
        liquido = float(pacote - desconto)
        print("O pacote de {}R$, para 2 pessoas tem desconto de: {}R$".format(pacote,desconto))
        print("Valor liquido: {} R$".format(liquido))
    elif pessoa >= 4:
        desconto = float(pacote * 0.20)
        liquido = float(pacote - desconto)
        print("O pacote de {}R$, para 2 pessoas tem desconto de: {}R$".format(pacote,desconto))
        print("Valor liquido: {} R$".format(liquido))

else:
    print("categoria de assento inválida... Tente novamente!")