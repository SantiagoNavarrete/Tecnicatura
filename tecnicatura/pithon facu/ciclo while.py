#contador = 0 
#while contador < 3:
#    print("Ejecutamos nuestro ciclo while ", contador)
#    contador += 1
#else:
#    print("Fin ciclo while")
#maximo = 5 
#contador = 0 
#while contador <= maximo:
#    print(contador)
#    contador += 1
#minimo = 1
#contador = 5
#while contador >= minimo:
#    print(contador)
#    contador -= 1
#
#cadena = "Hello"
#for letra in cadena:
#    print(letra)
#else: print("fin del ciclo for")
#for letra in "alemania":
#    if letra == "a":
#        print(" ")
#        print(f"Letra encontrada: {letra}")
#        break
#    else:
#        print("Fin del ciclo for")
for i in range (6):
    if i % 2 != 0:
        continue
    print (f"Valor: {i}")
    