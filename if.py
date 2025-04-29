# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales


#numero1 = input("Escribe un numero ")
#numero2 = input("Escribre otro numero ")

#if numero1 < numero2:
#    print(f"El numero mayor es {numero2}")
#elif numero1 > numero2:
#    print(f"El numero mayor es {numero1}")
#else:
#    print("Los numeros son iguales")



# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

#numero1 = input("Escribe un numero ")
#numero2 = input("Escribre otro numero ")
#operacion = input("Escribe una operacion ")

#if operacion == "+":
#    print(int(numero1) + int(numero2))
#elif operacion == "-":
#    print(int(numero1) - int(numero2))
#elif operacion == "*":
#    print(int(numero1) * int(numero2))
#elif operacion == "/" and int(numero2) == 0:
#    print("No se puede dividir por 0")
#elif operacion == "/":
#    print(int(numero1) / int(numero2))

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("introduzca una edad "))

if 0 <= edad <= 2:
    print("Bebé")
elif edad <= 12:
    print("Niño")
elif edad <= 17:
    print("Adolescente")
elif edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")
else:
    print("Edad no válida")