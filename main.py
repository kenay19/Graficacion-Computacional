import lines.lines as l 
import numpy as np 

def menuLines():
    option = "s"
    while option == "s" or option == "S":
        print("="*50)
        x = int(input("Da el tamaño en X de la matriz: ")) +1
        y = int(input("Da el tamaño en Y de la matriz: ")) +1   
        mat = np.zeros((x, y),np.uint8)
        print("="*50)
        print("1) Metodo de Linea Basica")
        print("2) Metodo de Linea Incremental")
        print("3) Metodo de DDA")
        print("4) Metodo de Bresenham")
        print("5) Metodo de linea doble")
        option = int(input("Escoge una Opcion: "))
        if option == 1:
            l.lineBasic(mat,[int(input("X1: ")), int(input("Y1: "))],[int(input("X2: ")), int(input("Y2: "))])
        elif option == 2:
            l.incremental(mat,[int(input("X1: ")), int(input("Y1: "))],[int(input("X2: ")), int(input("Y2: "))])
        elif option == 3:
            l.dda(mat,[int(input("X1: ")), int(input("Y1: "))],[int(input("X2: ")), int(input("Y2: "))])
        elif option == 4:
            l.bresenham(mat,[int(input("X1: ")), int(input("Y1: "))],[int(input("X2: ")), int(input("Y2: "))])
        elif option == 5:
            l.doubleline(mat,[int(input("X1: ")), int(input("Y1: "))],[int(input("X2: ")), int(input("Y2: "))])
        option = input("Desea Realizar Otra Operacion de Lineas (s/n): ")
   

def chooseOption():
    option = "s"
    while option == "s" or option =="S":
        print("1) Lineas")
        print("="*50)
        option = int(input("Escoge una operacion: "))
        if option == 1:
            menuLines()
        option = input("Desea Realizar Otra Operacion (s/n): ") 

chooseOption()