#miVaraible = 3; 
#print(miVaraible)
#miVaraible = "Hola a todos los estudiantes de la tecnicatura";
#print(miVaraible)
#miVaraible = 3.5;
#print(miVaraible)
#x = 10
#y = 2
#z = x+y 
#print(id(x))
#
##las literales se escribe x183
#print(id(y))
#print(id(x))
#
##tipos int, float, String, bool
#x = 10 
#print(x)
#print(type(x))
#x = 14.5 
#print(x)
#print(type(x))
#x = "Hola almunos"
#print(type(x))
#x = True
#print(x)
#print(type(x))
#
##Manejo de cadenas(String)
#miGrupoFavorito = "The Lether Black: "
#caracteristicas = "The Best Rock Band"
#print("Mi grupo favorito es: ", miGrupoFavorito, caracteristicas)
#numero1 = "7"
#numero2 = "8"
#print(int(numero1) + int(numero2))
#Tipos booleanos
#miBooleano = 1 > 2; 
#print(miBooleano)
#if miBooleano:
#    print("El resultado es verdadero")
#else:
#    print("El resulta es falso ")
#    
##Resultado = input("Didite un numero: ")
#print(Resultado)

#numero1 = int(input("Digite el primer numero: "));
#numero2 =int(input("Digite el segundo numero: "));
#resultado = numero1 + numero2
#print("El resultado de la suma: ", resultado)

#operandoA = 8
#operandoB = 5
#suma = operandoA+ operandoB
##print("El resultado de la suma: ", suma)
#print(f' El resultado de la suma es ', {suma})
#resta = operandoA - operandoB
#print(f' El resultado de la resta es ', {resta})
#multiplicacion = operandoA * operandoB
#print(f' El resultado de la multiplicacion es ', {multiplicacion})
#division = operandoA / operandoB
#print(f' El resultado de la division es ', {division})
#division operandoA // operandoB
#print(f' El resultado de la (int) division es ', {division})
#modulo = operandoA % operandoB
#print(f' El resultado de la division o residuo (modulo) es ', {modulo})
#
#exponente = operandoA ** operandoB
#print(f' El resultado de la division o residuo (modulo) es ', {exponente})
#
#alto = int(input("Digite el alto del rectangulo: "))
#ancho = int(input("Digite el ancho del rectangulo: "))
#area = alto * ancho
#perimetro = (alto + ancho) *2
#print("El area es: ", area)
#print("El perimetro es: ", perimetro)

#miVariable3 = 10; 
#print(miVariable3)
#
##operadores de reasignacion
#miVariable3 = miVariable3+1 
#print(miVariable3)
#
#miVariable3 += 1
#print(miVariable3)
#
#miVariable3 -= 2
#print(miVariable3)
#
#miVariable3 *= 3
#print(miVariable3)
#
#miVariable3 /= 2
#print(miVariable3)
#
## Operadores de comparacion
#
#d = 4
#b = 2
#resultado = d==b #comprobamos si son iguales
#print(resultado)
#
#resultado = d != b
#print(resultado)
#
#resultado = d > b
#print(resultado)
#
#resultado = d < b
#print(resultado)
#
#resultado = d <= b
#print(resultado)

#a = int(input("DIGITE UN NUMERO:  "))
#print("El residuo de la division es: ", a % 2)
#if a % 2 == 0: 
#    print(f"El valor de a es: {a} es un numero PAR")
#else: 
#    print(f"El valor de a es: {a} es un numero IMPAR")
#edadAdulto = 18
#edadtuya = int(input("Digite su edad: "))
#if edadAdulto>edadtuya:
#    print("Sos menor de edad")
#else: 
#    print("Sos mayor de edad")  
#Operador AND 
#a = True
#b = True
#resultado = a and b
#print(resultado)
##Operador OR
#resultado = a or b
#print(resultado)
##Operador NOT 
#resultado = not a
#print(resultado)
#valor = int(input("Digite un numero: "))
#valorMinimo = 0
#valorMaximo = 5
#dentroRango = valor>= valorMinimo and valor <= valorMaximo
#if dentroRango: 
#    print(f"El valor {valor} esta dentro del rango")
#else:
#    print(f"El valor {valor} esta fuera de rango")
#vacaciones = True
#diaDeDescanso = True
#if not (vacaciones or diaDeDescanso):
#    print("Tiene trabajo que hacer")
#else:
#    print("Puede asistir al juego")
#edad = int(input("Digite su edad: "))
#veinte = edad >= 20 and edad < 30
#print(veinte)
#treinta = edad >= 30 and edad < 40
#print(treinta)
#if veinte or treinta:
#    if veinte:
#        print(" Estas dentro del rango (20\'0) años")
#    elif treinta:
#        print(" Estas dentro del rango (30\'0) años")
#    else:
#        print("no estas dentro del rango (20'0) a (30'0) años") 
#numero1 = int(input("Digite el primer numero: "))
#numero2 = int(input("Digite el segundo numero: "))
#if numero1 > numero2:
#    print("El numero 1 es mayor")
#else:
#    print("El numero 2 es mayor")
#print("Digite los siguientes datos de un libro")
#nombre = input("Digite el nombre del libro: ")
#id = int(input("Digite el ID del libro: "))
#precio = int(input("Digite el precio del libro: "))
#envioGratuito = input("Indique si el envio es gratuito True/False: ")
#if envioGratuito == "True":
#    envioGratuito== True
#    
#elif envioGratuito == 1"False":
#    envioGratuito == False
#else: envioGratuito = "El valor es incorrecto, debe escribir True/False"
#print(f"""
#      Nombre: {nombre}
#      ID: {id}
#      precio: {precio}
#      Envio: {envioGratuito}
#""")
#condicion = 10
#if condicion == True:
#    print("Condicion verdadera ")
#elif condicion == False:
#    print("La condicion es falsa")
#else:
#    print("condicion sin especificar")
#num = int(input('Digite un numero del rango del 1 al 3: '))
#numTexto = ''
#if num == 1:
#    numTexto = 'NUMERO 1'
#elif num == 2:
#    numTexto = 'NUMERO 2'
#elif num == 3:
#    numTexto = 'NUMERO 3'
#else:
#    numTexto = 'El numero ingresado no esta disponible en la escala del 1 al 3'
#print(f'El numero ingresado es: {num} - {numTexto}')
#a = float(input("Digite el valor de a"))
#b = float(input("Digite el valor de b"))
#c = float(input("Digite el valor de c"))
#resultado = (a ** 3 * (b ** 2 - 2 * a * c)) / (2 * b)
#print("EL resultado es: ", resultado)
condicion = False
if condicion:
    print("Condicion verdadera")
else:
    print("Condicion falsa")
    
print("Condicion verdadera") if condicion else ("Condicion falsa")