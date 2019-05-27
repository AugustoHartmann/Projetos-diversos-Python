pares = 0
impares = 0
codigo = input("Insira aqui o número do código de barras (sem pontos ou traços): ")
if len(codigo) <= 12:
    print("Há digitos faltando...")
for i in range(1,13):
    if i%2 == 0:
        pares += int(codigo[(i-1):i])
    else:
        impares += int(codigo[(i-1):i])
tpares = pares*3
timpares = impares
total = tpares + timpares
for i in range(1,11):
    if total > 10*i:
        resultado = total - (10*(i+1))
nresultado = int(resultado*-1)
ultimodigito = int(codigo[int(len(codigo))-1:int(len(codigo))])
if nresultado == ultimodigito:
    print("O código e seu dígito verificador são válidos")
else:
    print("O código e seu dígito verificador estão em desaranjo")
    print("O dígito verificador correto é:" ,nresultado)
