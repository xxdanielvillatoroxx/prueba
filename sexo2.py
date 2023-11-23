def opcion1():
        print("esta es la op1")

def opcion2():
     print("esta es la op2")

def Menu():
    print("Seleccione una opcion")
    print("[1] opcion 1")
    print("[2] opcion 2")
    
Menu()

teclado = int(input("Ingrese una de las dos opciones"))

while teclado != 0:
    if teclado == 1:
        opcion1()
    elif teclado == 2:
         opcion2()
    else:
         print("ponga el bueno")
    Menu() 
    teclado = int(input("Ingrese una de las dos opciones"))
     



