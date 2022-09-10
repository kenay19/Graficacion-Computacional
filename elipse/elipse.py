import numpy as np
def fourPoitns(mat,p,rx,ry):
    x = p[0]
    y = p[1]
    mat[ x + rx , y + ry ] = 255
    mat[ x + rx , y - ry ] = 255
    mat[ x - rx , y + ry ] = 255
    mat[ x - rx , y - ry ] = 255
    return mat

def basicElipses(mat,p,rx,ry):
    x = 0
    y = ry
    f = ry 
    while (ry**2) * x < (rx**2) * f:
        mat = fourPoitns(mat,p,f,x) 
        x = x + 1 
        y = (ry/rx)*np.sqrt((rx**2) - (x**2))
        f = int(y  + 0.5)
    y = 0 
    x = rx
    f = rx
    while (ry**2)*f >= (rx**2)*y:
        mat = fourPoitns(mat,p,y,f)
        y = y + 1
        x = (rx/ry)*np.sqrt((ry**2) - (y**2))
        f = int(x + 0.5)
    return mat

def bresenhamElipse(mat,p,rx,ry):
    x = 0 
    y = ry 
    d = ry**2 - rx**2 * ry + 1/4 * rx**2 
    while ry**2 * x < rx**2 * y:
        mat = fourPoitns(mat,p,y,x)
        if d < 0: 
            d =  d + ry**2 * (2*x +3 )
        else: 
            d = d + ry**2 * (2*x +3) + 2*rx**2 * (1-y)
            y = y - 1 
        x = x +1 
    x = rx 
    y = 0 
    d = d = rx**2 - ry**2 * rx + 1/4 *ry**2 
    while ry**2 *x >= rx**2 * y :
        mat = fourPoitns(mat,p,y,x)
        if d <  0:
            d = d + rx**2 * (2*y +3)
        else:
            d = d + rx**2 * (2* y + 3 ) + 2*ry**2 * (1-x)
            x = x - 1
        y = y +1 
    return mat

def bresenhamElipseMod(mat,p,rx,ry):
    x = 0 
    y = ry 
    h = int(ry**2 + rx**2 * ry + 1/4 * rx**2 + 0.5)
    while (ry**2) * x < rx**2 * y :
        mat = fourPoitns(mat,p,y,x)
        if h <  0:
            h = h + ry**2 * (2*x+3)
        else:
            h = h + ry**2 * (2*x +3) + 2*rx**2 * (1 - y)
            y = y - 1
        x = x +1 
    x = rx 
    y = 0 
    h = int(rx**2 - ry**2 * rx + 1/4 * ry**2)
    while ry**2 * x >=  rx**2* y:
        mat =   fourPoitns(mat,p,y,x)
        if h  <  0:
            h = h + rx**2 * (2 * y + 3)
        else:
            h = h + rx**2 * (2*y +3) + 2*ry**2 * (1-x)
            x = x -1 
        y = y + 1
    return mat