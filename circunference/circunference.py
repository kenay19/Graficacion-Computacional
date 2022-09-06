import cv2 as c 
import numpy as np

def ochopuntos(mat,p1,p2):
    xc = p1[0]
    x = p2[0]
    yc = p1[1]
    y = p2[1]
    mat[ xc + x , yc + y ] = 255
    mat[ xc - x , yc + y ] = 255
    mat[ xc + x , yc - y ] = 255
    mat[ xc - x , yc - y ] = 255
    mat[ xc + y , yc + x ] = 255
    mat[ xc - y , yc + x ] = 255
    mat[ xc + y , yc - x ] = 255
    mat[ xc - y , yc - x ] = 255
    return mat

def BasicCircle(mat,p1,r):
    x = 0 
    y = r 
    f = r 
    while x <= f :
        mat = ochopuntos(mat,p1,[x,f]) 
        x = x + 1 
        y = np.sqrt(r**2 - x**2)
        f = int(y + 0.5)
    return mat
    
def BersenhamCircles(mat,p1,r): 
    x = 0
    y = r 
    d = (5/4) - r 
    while x <= y :
        mat = ochopuntos(mat,p1,[x,y]) 
        if d <  0:
            d = d + 2*x +3
        else: 
            d = d + 2*(x-y) + 5
            y = y-1
        x = x+1 
    return mat

def BresenhamCirclesModified(mat,p1,r):
    x = 0
    y = r
    h = 1 - r 
    while x <=  y :
        mat = ochopuntos(mat,p1,[x,y])
        if h <  0:
            h = h + 2 * x + 3
        else:
            h = h + 2*(x -y) + 5
            y = y - 1
        x = x + 1 
    return mat

mat =np.zeros((500,500),np.uint8)
    

#ochopuntos(mat,[int(input("X1: ")), int(input("Y1: "))],[int(input("X2: ")), int(input("Y2: "))])
#BresenhamCirclesModified(mat,[int(input("X1: ")), int(input("Y1: "))],int(input("r: ")))