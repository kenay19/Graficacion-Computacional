import lines.lines as l 
import circunference.circunference as c 
import elipse.elipse as el
import numpy as np 
import auxiliar as aux

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
        print("6) Cohen-Sutherland linea tipo Clipping")
        print("7) Sutherland-hodgman poligono tipo Clipping")
        option = int(input("Escoge una Opcion: "))
        if option == 1:
            result = l.lineBasic(mat,[int(input("X1: ")), int(input("Y1: "))],[int(input("X2: ")), int(input
            ("Y2: "))])
            name = "Linea Basica"
        elif option == 2:
            result = l.incremental(mat,[int(input("X1: ")), int(input("Y1: "))],[int(input("X2: ")), int(input("Y2: "))])
            name = "Linea Incremental"
        elif option == 3:
            result = l.dda(mat,[int(input("X1: ")), int(input("Y1: "))],[int(input("X2: ")), int(input("Y2: "))])
            name = " Metodo DDA"
        elif option == 4:
            result = l.bresenham(mat,[int(input("X1: ")), int(input("Y1: "))],[int(input("X2: ")), int(input("Y2: "))])
            name = "Metodo de Bresenham"
        elif option == 5:
            result = l.doubleline(mat,[int(input("X1: ")), int(input("Y1: "))],[int(input("X2: ")), int(input("Y2: "))])
            name = "Metodo de la linea doble"
        elif option == 6:
            result = l.recortLine(mat,[int(input("X1: ")), int(input("Y1: "))],[int(input("X2: ")), int(input("Y2: "))])
            name = "Cohen-Sutherland linea tipo Clipping"   
            result = l.recortLine(result,[int(input("X1: ")), int(input("Y1: "))],[int(input("X2: ")), int(input("Y2: "))])        
            result = l.recortLine(result,[int(input("X1: ")), int(input("Y1: "))],[int(input("X2: ")), int(input("Y2: "))])
        elif option == 7:
            name = "Sutherland-hodgman poligono tipo Clipping"
            result = l.recortLineHodgman(mat)
        aux.graficmatriz(result, name)
        option = input("Desea Realizar Otra Operacion de Lineas (s/n): ")

def menucircles():
    option = "s"
    while option == "s" or option == "S":
        print("="*50)
        x = int(input("Da el tamaño en X de la matriz: ")) +1
        y = int(input("Da el tamaño en Y de la matriz: ")) +1   
        mat = np.zeros((x, y),np.uint8)
        print("="*50)
        print("1) Ocho Puntos")
        print("2) Circulo Basico")
        print("3) Circulos de Bresenham")
        print("4) Circulos de Bresenham Modificado")
        option = int(input("Escoge una Opcion: "))
        if option == 1 : 
            result = c.ochopuntos(mat,[int(input("X1: ")), int(input("Y1: "))],[int(input("X2: ")), int(input
            ("Y2:"))])
            name="Ocho Puntos"
        elif option == 2:
            result = c.BasicCircle(mat,[int(input("X1: ")), int(input("Y1: "))],int(input("R: ")))
            name = "Circulos Basico"
        elif option == 3:
            result = c.BersenhamCircles(mat,[int(input("X1: ")), int(input("Y1: "))],int(input("R:")))
            name = "Metodo de Bresenham"
        elif option == 4:
            result = c.BresenhamCirclesModified(mat,[int(input("X1: ")), int(input("Y1: "))],int(input("R:")))
            name = "Metodo de Bresenham modificado"
        aux.graficmatriz(result, name)
        option = input("Desea Realizar Otra Operacion de Circulos (s/n): ") 

def menuElpises():
    option = "s"
    while option == "s" or option == "S":
        print("="*50)
        x = int(input("Da el tamaño en X de la matriz: ")) +1
        y = int(input("Da el tamaño en Y de la matriz: ")) +1   
        mat = np.zeros((x, y),np.uint8)
        print("="*50)
        print("1) Cuatro Puntos")
        print("2) Elipse Basico")
        print("3) Elipse de Bresenham")
        print("4) Elipse de Bresenham Modificado")
        option = int(input("Escoge una Opcion: "))
        if option == 1 : 
            result = el.fourPoitns(mat,[int(input("X1: ")), int(input("Y1: "))],int(input("rx: ")), int(input("ry: ")))
            name="cuatro Puntos"
        elif option == 2:
            result = el.basicElipses(mat,[int(input("X1: ")), int(input("Y1: "))],int(input("rx: ")),int(input("ry: ")))
            name = "elipse Basico"
        elif option == 3:
            result = el.bresenhamElipse(mat,[int(input("X1: ")), int(input("Y1: "))],int(input("rx:")), int(input("ry: ")))
            name = "Elipse de Bresenham"
        elif option == 4:
            result = el.bresenhamElipseMod(mat,[int(input("X1: ")), int(input("Y1: "))],int(input("rx: ")), int(input("ry: ")))
            name = "Elipse de Bresenham modificado"
        aux.graficmatriz(result, name)
        option = input("Desea Realizar Otra Operacion de Circulos (s/n): ") 

def menuFirstParcial():
    option = "s"
    while option == "s" or option == "S":
        print("="*50)
        x = int(input("Da el tamaño en X de la matriz: ")) +1
        y = int(input("Da el tamaño en Y de la matriz: ")) +1   
        mat = np.zeros((x, y),np.uint8)
        print("="*50)
        print("1) Linea")
        print("2) Poligono")
        option = int(input("Escoge una Opcion: "))
        if option == 1:
            result = l.line(mat)
            name = "Linea examen primer parcial"
        if option == 2:
            result = l.poligono(mat,int(input("Xc: ")),int(input("Yc: ")),int(input("Radio:")),int(input("lados:")))
            name = "Poligono exame primer parcial"
        aux.graficmatriz(result, name)
        option = input("Desea Realizar Otra Operacion de Lineas (s/n): ")

    option = "s"
    while option == "s" or option == "S":
        print("="*50)
        x = int(input("Da el tamaño en X de la matriz: ")) +1
        y = int(input("Da el tamaño en Y de la matriz: ")) +1   
        mat = np.zeros((x, y),np.uint8)
        print("="*50)
        print("1) Cuatro Puntos")
        print("2) Elipse Basico")
        print("3) Elipse de Bresenham")
        print("4) Elipse de Bresenham Modificado")
        option = int(input("Escoge una Opcion: "))
        if option == 1 : 
            result = el.fourPoitns(mat,[int(input("X1: ")), int(input("Y1: "))],int(input("rx: ")), int(input("ry: ")))
            name="cuatro Puntos"
        
        aux.graficmatriz(result, name)
        option = input("Desea Realizar Otra Operacion de Circulos (s/n): ") 

def chooseOption():
    option = "s"
    while option == "s" or option =="S":
        print("1) Lineas")
        print("2) Circulos")
        print("3) Elipses")
        print("4) Examen Primer Parcial")
        print("="*50)
        option = int(input("Escoge una operacion: "))
        if option == 1:
            menuLines()
        elif option == 2:
            menucircles()
        elif option == 3:
            menuElpises()
        elif option == 4:
            menuFirstParcial()
        option = input("Desea Realizar Otra Operacion (s/n): ") 


chooseOption()