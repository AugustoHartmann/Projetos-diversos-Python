def cpf():
    cpf = input("Insira aqui o CPF a ser analisado: ")
    soma = 0
    valor = (int(cpf[0:1])*10)+(int(cpf[1:2])*9)+(int(cpf[2:3])*8)+(int(cpf[3:4])*7)+(int(cpf[4:5])*6)+(int(cpf[5:6])*5)+(int(cpf[6:7])*4)+(int(cpf[7:8])*3)+(int(cpf[8:9])*2)
    soma = soma + valor
    arredondamento = soma%11
    if arredondamento == 0 or arredondamento == 1:
        penultimo = 0
    penultimo = 11 - arredondamento
    soma2 = 0
    if penultimo == int(float(cpf[-2])):
        valor2 = (int(cpf[0:1])*11)+(int(cpf[1:2])*10)+(int(cpf[2:3])*9)+(int(cpf[3:4])*8)+(int(cpf[4:5])*7)+(int(cpf[5:6])*6)+(int(cpf[6:7])*5)+(int(cpf[7:8])*4)+(int(cpf[8:9])*3)++(int(cpf[9:10])*2)
        soma2 = soma2 + valor2
        arredondamento2 = soma2%11
        if arredondamento == 0 or arredondamento == 1:
            ultimo = 0
        ultimo = 11- arredondamento2
        print("CPF Válido")
    else:
        print("CPF Inválido")
cpf()

