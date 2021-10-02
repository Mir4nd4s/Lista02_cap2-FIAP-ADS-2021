print("Vote entre as opções: Playstaton, Xbox, Nintendo")
v1 = input("Digite o 1º voto: ")
v2 = input("Digite o 2º voto: ")
v3 = input("Digite o 3º voto: ")
v4 = input("Digite o 4º voto: ")
v5 = input("Digite o 5º voto: ")

vp1 = 0
vp2 = 0
vp3 = 0
vp4 = 0
vp5 = 0
vn1 = 0
vn2 = 0
vn3 = 0
vn4 = 0
vn5 = 0
vx1 = 0
vx2 = 0
vx3 = 0
vx4 = 0
vx5 = 0

if v1.upper() == "PLAYSTATION":
    vp1 = 1
elif v1.upper() == "XBOX":
    vx1 = 1
elif v1.upper() == "NINTENDO":
    vn1 = 1
else:
    print("Opção inválida do voto 1!")

if v2.upper() == "PLAYSTATION":
    vp2 = 1
elif v2.upper() == "XBOX":
    vx2 = 1
elif v2.upper() == "NINTENDO":
    vn2 = 1
else:
    print("Opção inválida do voto 2!")

if v3.upper() == "PLAYSTATION":
    vp3 = 1
elif v3.upper() == "XBOX":
    vx3 = 1
elif v3.upper() == "NINTENDO":
    vn3 = 1
else:
    print("Opção inválida do voto 3!")

if v4.upper() == "PLAYSTATION":
    vp4 = 1
elif v4.upper() == "XBOX":
    vx4 = 1
elif v4.upper() == "NINTENDO":
    vn4 = 1
else:
    print("Opção inválida do voto 4!")

if v5.upper() == "PLAYSTATION":
    vp5 = 1
elif v5.upper() == "XBOX":
    vx5 = 1
elif v5.upper() == "NINTENDO":
    vn5 = 1
else:
    print("Opção inválida do voto 5!")

vp = (vp1 + vp2 + vp3 + vp4 + vp5)
vx = (vx1 + vx2 + vx3 + vx4 + vx5)
vn = (vn1 + vn2 + vn3 + vn4 + vn5)

maior = 0

if vp > vx and vp > vn:
    maior = vp
    print("mais votado Playstation com: {} votos".format(maior))
elif vn > vp and vn > vx:
    maior = vn
    print("mais votado nintendo com: {} votos".format(maior))
elif vx > vp and vx > vn:
    maior = vx
    print("mais votado Xbox com: {} votos".format(maior))
else:
    if vp == vx:
        print("Houve empate: Playstation ({}), Xbox ({})" .format(vp,vx))
    elif vp == vn:
        print("Houve empate: Playstation ({}),  Nintendo ({})" .format(vp,vn))
    elif vn == vx:
        print("Houve empate: Nintendo ({}),  Xbox ({})" .format(vn,vx))
















