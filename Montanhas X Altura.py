montanhas = {}
for i in range(0,2):
    nome = input("Insira o nome da montanha: ")
    alturam = input("Insira a altura dela em metros: ")
    alturap = input("Insira a altura dela em pés: ")
    montanhas[nome] = [alturam, alturap]
for nome in montanhas:
    print("Nome: ",nome,"   Altura em metros:",(montanhas[nome][0]))
    print("Nome: ",nome,"   Altura em pés:",(montanhas[nome][1]))
    print("")
