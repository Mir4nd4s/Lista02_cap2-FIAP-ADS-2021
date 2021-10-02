# Criei a faixa de 3 à 7 anos com os parametros de 100 a 120 BPM

print("*Verificação de batimentos por minuto [BPM]*\nOlá Usuário!")
idade = float(input("Informe sua idade: "))
bpm = float(input("Informe o seu número de batimentos por minuto (BPM): "))

if idade <= 2:
    if bpm < 120:
        print("Seus batimentos encontram-se ABAIXO da faixa adequada!")
    elif bpm < 140:
        print("Seus batimentos encontram-se DENTRO da faixa adequada!")
    else:
        print("Seus batimentos encontram-se ACIMA da faixa adequada!")
if idade > 3 and idade <= 7:
    if bpm < 100:
         print("Seus batimentos encontram-se ABAIXO da faixa adequada!")
    elif bpm < 120:
        print("Seus batimentos encontram-se DENTRO da faixa adequada!")
    else:
         print("Seus batimentos encontram-se ACIMA da faixa adequada!")
elif idade >= 8 and idade <= 17:
    if bpm < 80:
        print("Seus batimentos encontram-se ABAIXO da faixa adequada!")
    elif bpm < 100:
        print("Seus batimentos encontram-se DENTRO da faixa adequada!")
    else:
        print("Seus batimentos encontram-se ACIMA da faixa adequada!")
elif idade >= 18 and idade <= 65:
    if bpm < 70:
        print("Seus batimentos encontram-se ABAIXO da faixa adequada!")
    elif bpm < 80:
        print("Seus batimentos encontram-se DENTRO da faixa adequada!")
    else:
        print("Seus batimentos encontram-se ACIMA da faixa adequada!")
elif idade > 65:
    if bpm < 50:
        print("Seus batimentos encontram-se ABAIXO da faixa adequada!")
    elif bpm < 60:
        print("Seus batimentos encontram-se DENTRO da faixa adequada!")
    else:
        print("Seus batimentos encontram-se ACIMA da faixa adequada!")



