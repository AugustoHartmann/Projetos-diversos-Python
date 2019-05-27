import random
print("Sorteando números...")
numerossorteados = {}
for i in range(1,100000):
    for i in range(1,6):
        numero = random.randint(1,60)
        numerossorteados[numero] = numerossorteados.get(numero,0)+1
print(numerossorteados)
