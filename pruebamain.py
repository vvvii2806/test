from prueba129.pruebanoseque import EstoyProbandoWeas

gambling1 = EstoyProbandoWeas("balarto",100)
gambling2 = EstoyProbandoWeas("nose?",100)

print(gambling1,gambling2)
gambling1.gambling(4)
gambling2.gambling(4)

if gambling1.puntos > gambling2.puntos:
    print("gana 1")
else:
    print("xd")