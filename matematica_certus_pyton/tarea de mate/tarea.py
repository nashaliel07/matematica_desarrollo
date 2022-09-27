# SEGUNDO PROYECTO UNA CALCULADORA EN PYTHON 
# TITULO : CALCULADORA BASICA DE PYTHON
# en esta calculadora pordras sumar, restar y multiplicar, ayudara a facilitar en las ecuaciones de suma resta y multiplicacion
# acontinuacion el codigo: 

n1 = float(input("primer numero: "))
n2 = float(input("segundo numero: "))
while True:
    print(""" Opcines: 
        1) Suma
        2) Resta
        3) Multiplicar
        4) Salir """)
    opcion = int(input("ingresa operacion realizada"))
    if opcion == 1:
        print("la suma es : ", n1 + n2)
        print("¿desea realizar otra operacion? s/n ")
        rpta = input()
        if rpta == "s":
            continue
        else:
            break
    elif opcion == 2:
        print("la resta es : ", n1 - n2)
        print("¿desea realizar otra operacion? s/n ")
        rpta = input()
        if rpta == "s":
            continue
        else:
            break
    if opcion == 3:
        print("la resta es : ", n1 * n2)
        print("¿desea realizar otra operacion? s/n ")
        rpta = input()
        if rpta == "s":
            continue
        else:
            break

    else:
        opcion == 4
        print("gracias por entrar")
    if rpta == "n":
        break
