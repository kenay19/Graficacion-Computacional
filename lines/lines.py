import cv2 as c
import math as ma
import numpy as np 

def lineBasic(mat,p1,p2):
    m = (p1[1]-p2[1])/(p1[0]-p2[0])
    for i in range(p1[0],p2[0],1):
        Y = m*(i-p1[0])+p1[1]
        mat[int(Y+0.5),i] = 255
    return mat

def incremental(mat,p1, p2):
    print(p1,p2)
    if p1[0] == p2[0]:
        print("a")
        mat[p1[1]:p2[1],p1[0]] = 255
    elif p1[1] == p2[1]:
        print("b")
        mat[p1[1],p1[0]:p2[0]] = 255
    else:
        print("c")
        m = (p1[1]-p2[1])/(p1[0]-p2[0])
        y = p1[1]
        for x in range(p1[0],p2[0]):
            mat[ma.floor(y+0.5),x] = 255
            y = y + m 
    return mat

def dda(mat,p1,p2):
    if p1[0] == p2[0]:
        mat[p1[1]:p2[1],p1[0]] = 255
    elif p1[1] == p2[1]:
        mat[p1[1],p1[0]:p2[0]] = 255
    else:
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if abs(dx) < abs(dy) :
            paso = abs(dy)
        else:
            paso = abs(dx)
        xInc = dx/paso
        yInc = dy/paso
        mat[p1[1],p1[0]] = 255
        x = p1[0] 
        y = p1[1]
        for i in range(paso):
            x = x + xInc
            y = y + yInc
            mat[int(y),int(x)] = 255 
    return mat

def bresenham(mat,p1,p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    p = 2*dy-dx
    c1 = 2*dy
    c2 = 2*(dy-dx)
    if p1[0] > p2[0]:
        x = p2[0]
        y = p2[1]
        xFin = p1[0]
    else:
        x = p1[0]
        y = p1[1]
        xFin = p2[0]
    mat[y,x] = 255
    while x < xFin:
        x = x+1 
        if p < 0:
            p = p +c1
        else:
            y = y+1 
            p = p + c2 
        mat[y,x] = 255
    m = (p2[1]-p1[1])/(p2[0]-p1[0])
    y = p1[1]
    for i in range(p1[0],p2[0],1):
        mat[int(y+0.5),x]
        i =i+1
        y = y+m
    return mat

def doubleline(mat,p1,p2):
    mat = lineBasic(mat,p1,p2)
    mat = lineBasic(mat,[p1[0]+1,p1[1]],[p2[0]+1,p2[1]])
    mat = lineBasic(mat,[p1[0],p1[1]+1],[p2[0],p2[1]+1])
    mat = lineBasic(mat, [p1[0]+1,p1[1]+1] , [p2[0]+1,p2[1]+1])
    return mat

def generateCode(x,y,xmin,ymin,xmax,ymax):
    code = ""
    if y > ymax:
        code = code + "1"
    else:
        code = code + "0"
    if y < ymin:
        code = code + "1"
    else:
        code = code + "0"
    if x > xmax : 
        code = code + "1"
    else:
        code = code + "0"
    if x < xmin:
        code = code + "1"
    else: 
        code = code + "0"
    return code

def verifyCodes(code1, code2):
    code = ""
    for i in range(len(code1)):
        if code1[i] == "1" and code2[i] == "1":
            code = code + "1"
        else:
            code = code + "0"
    return code 

def calculateX(y,x1,x2,y1,y2):
    return int(x1+((y-y1)/(y2-y1))*(x2-x1))

def calculateY(x,x1,x2,y1,y2):
    return int(y1+((x-x1)/(x2-x1))*(y2-y1))

def coordantes(x1,x2,y1,y2,xmin,ymin,xmax,ymax,code,point):
    if point == 1:
        x =x1
        y = y1
    if point == 2:
        x = x2
        y = y2 
    if code == "1001":
        if point == 1:
            x = calculateX(ymax,x1,x2,y1,y2)
            y = calculateY(xmin,x1,x2,y1,y2)
        else:
            x = calculateX(ymax,x2,x1,y2,y1)
            y = calculateY(xmin,x2,x1,y2,y1)
        if generateCode(xmin,y,xmin,ymin,xmax,ymax) == "0000":
            x = xmin
        if generateCode(x,ymax,xmin,ymin,xmax,ymax) == "0000":
            y = ymax
    if code == "0001":
        if point == 1:
            y = calculateY(xmin,x1,x2,y1,y2)
        else:
            y = calculateY(xmin,x2,x1,y2,y1)
        x = xmin
    if code == "0101":
        if point == 1:
            x = calculateX(ymin,x1,x2,y1,y2)
            y = calculateY(xmin,x1,x2,y1,y2)
        else:
            x = calculateX(ymin,x2,x1,y2,y1)
            y = calculateY(xmin,x2,x1,y2,y1)
        if generateCode(xmin,y,xmin,ymin,xmax,ymax) == "0000":
            x = xmin
        if generateCode(x,ymin,xmin,ymin,xmax,ymax) == "0000":
            y = ymin
    if code == "0100":
        if point == 1:
            x = calculateX(ymin,x1,x2,y1,y2)
        else:
            x = calculateX(ymin,x2,x1,y2,y1)
        y = ymin
    if code == "0110":
        if point == 1:
            x = calculateX(ymin,x1,x2,y1,y2)
            y = calculateY(xmax,x1,x2,y1,y2)
        else:
            x = calculateX(ymin,x2,x1,y2,y1)
            y = calculateY(xmax,x2,x1,y2,y1)
        if generateCode(xmax,y,xmin,ymin,xmax,ymax) == "0000":
            x = xmax
        if generateCode(x,ymin,xmin,ymin,xmax,ymax) == "0000":
            y = ymin
    if code == "0010":
        if point == 1:
            y = calculateY(xmax,x1,x2,y1,y2)
        else:
            y = calculateY(xmax,x2,x1,y2,y1)
        x = xmax
    if code == "1010":
        if point == 1:
            x = calculateX(ymax,x1,x2,y1,y2)
            y = calculateY(xmax,x1,x2,y1,y2)
        else:
            x = calculateX(ymax,x2,x1,y2,y1)
            y = calculateY(xmax,x2,x1,y2,y1)
        if generateCode(xmax,y,xmin,ymin,xmax,ymax) == "0000":
            x = xmax
        if generateCode(x,ymax,xmin,ymin,xmax,ymax) == "0000":
            y = ymax
    if code == "1000":
        if point == 1:
            x = calculateX(ymax,x1,x2,y1,y2)
        else:
            x = calculateX(ymax,x2,x1,y2,y1)
        y = ymax
    return x,y

def recortLine(mat,p1,p2,xmin,ymin,xmax,ymax):
    xsize,ysize = mat.shape
    mat = incremental(mat,[xmin,ymin],[xmax,ymin])
    mat = incremental(mat,[xmin,ymax],[xmax,ymax])
    mat = incremental(mat,[xmin,ymin],[xmin,ymax])
    mat = incremental(mat,[xmax,ymin],[xmax,ymax])
    ''' Formacion del Rectangulo Viewer'''
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
    code1 = generateCode(x1,y1,xmin,ymin,xmax,ymax)
    code2 = generateCode(x2,y2,xmin,ymin,xmax,ymax)
    if code1 == "0000" and code2 == "0000":
        mat = incremental(mat,[x1,y1],[x2,y2])
    elif verifyCodes(code1,code2) == "0000":
        if not(code1 == "0000"):
            p1 = coordantes(x1,x2,y1,y2,xmin,ymin,xmax,ymax,code1,1)
        if not(code2 == "0000"):
            p2 = coordantes(x1,x2,y1,y2,xmin,ymin,xmax,ymax,code2,2)
            mat = incremental(mat,list(p1),list(p2))
    else:
        mat = mat
    return mat

def line(mat) :
    b = True
    xaux = 0 
    yaux = 0 
    n = int(input("Introduce el Numero de puntos a graficar: "))
    for i in range(n):
        x = int(input("x"+str(i+1)+": "))
        y = int(input("y"+str(i+1)+": "))
        if b == True:
            b = False
            xaux = x
            yaux = y 
        else:
            mat = dda(mat,[xaux,yaux],[x,y])
            xaux = x
            yaux = y 
    return mat


    pass

def poligono(mat,xc,yc,r,l) :
    alfa = (2*ma.pi)/l
    x = []
    y = []
    a = 0 
    x.append(xc + int(r * np.cos((ma.pi/2) - a) +0.5))
    y.append(yc + int(r* np.sin((-ma.pi/2) - a) +0.5))
    for i in range(1,l):
        a = a + alfa
        x.append(xc +ma.floor(r * np.cos((ma.pi/2) - a) +0.5))
        y.append(yc + ma.floor(r* np.sin((-ma.pi/2) - a) +0.5))
        mat = dda(mat,[x[i-1],y[i-1]],[x[i],y[i]])
    mat = dda(mat,[x[0],y[0]],[x[l-1],y[l-1]])
    return mat

def recortLineHodgman(mat):
    xmin = int(input("xmin: "))
    xmax = int(input("xmax: "))
    ymin = int(input("ymin: "))
    ymax = int(input("ymax: "))
    mat = dda(mat,[xmin,ymin],[xmax,ymin])
    mat = dda(mat,[xmin,ymax],[xmax,ymax])
    mat = dda(mat,[xmin,ymin],[xmin,ymax])
    mat = dda(mat,[xmax,ymin],[xmax,ymax])
    n = int(input("Numero de puntos: "))
    points = []
    codes = []
    for i in range(n):
        xaux = int(input("X"+str(i)+": "))
        yaux = int(input("Y"+str(i)+": "))
        codes.append(generateCode(xaux, yaux,xmin,ymin,xmax,ymax))
        points.append([xaux,yaux])
    print(points)
    print(codes )
    vertices = []
    for i in range(len(points)):
        p1 = points[i]
        pant = points[i-1]
        if i == len(points) - 1:
            pdes = points[0]
        else:
            pdes = points[i+1]
        line1 = coordantes(p1[0],pant[0],p1[1],pant[1],xmin,ymin,xmax,ymax,codes[i],1)
        line2 = coordantes(p1[0],pdes[0],p1[1],pdes[1],xmin,ymin,xmax,ymax,codes[i],1)
        if not(compareList(vertices,line1)):
            vertices.append(line1)
        if not(compareList(vertices,line2)):
            vertices.append(line2)
    print(vertices)
    mat = dda(mat,vertices[0],vertices[-1])
    for i in range(1,len(vertices)):
        mat = dda(mat,vertices[i-1],vertices[i])
    mat = dda(mat,vertices[len(vertices)-2],vertices[len(vertices)-1])
    return mat

def compareList(lista,element):
    for i in range(len(lista)):
        if lista[i] == element:
            return True
    return False