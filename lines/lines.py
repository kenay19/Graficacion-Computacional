from this import d
from turtle import goto
import cv2 as c
import sys 
sys.path.append("src")
import auxiliar as aux

def lineBasic(mat,p1,p2):
    m = (p1[1]-p2[1])/(p1[0]-p2[0])
    for i in range(p1[0],p2[0],1):
        Y = m*(i-p1[0])+p1[1]
        mat[int(Y+0.5),i] = 255
    return mat

def incremental(mat,p1, p2):
    if p1[0] == p2[0]:
        mat[p1[1]:p2[1],p1[0]] = 255
    elif p1[1] == p2[1]:
        mat[p1[1],p1[0]:p2[0]] = 255
    else:
        m = (p1[1]-p2[1])/(p1[0]-p2[0])
        y = p1[1]
        for x in range(p1[0],p2[0],1):
            mat[int(y+0.5),x] = 255
            y = y + m 
    return mat

def dda(mat,p1,p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    if abs(dx) < abs(dy) :
        paso = abs(dy)
    else:
        paso = abs(dx)
    xInc = dx/paso
    yInc = dy/paso
    mat[p1[0],p1[1]] = 255
    x = p1[0] 
    y = p1[1]
    for i in range(paso):
        x = x + xInc
        y = y + yInc
        mat[int(x),int(y)] = 255 
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
    mat[x,y] = 255
    while x < xFin:
        x = x+1 
        if p < 0:
            p = p +c1
        else:
            y = y+1 
            p = p + c2 
        mat[x,y] = 255
    m = (p2[1]-p1[1])/(p2[0]-p1[0])
    y = p1[1]
    for i in range(p1[0],p2[0],1):
        mat[x,int(y+0.5)]
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
    x = 0 
    y = 0
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


def recortLine(mat,p1,p2):
    xsize,ysize = mat.shape
    xmin = int(input("Da xmin < "+str(xsize) + " : "))
    xmax = int(input("Da xmax < "+str(xsize) + " : "))
    ymin = int(input("Da ymin < "+str(ysize) + " : "))
    ymax = int(input("Da ymax < "+str(ysize) + " : "))
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
    return mat

 