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
        mat = fourPoitns(mat,p,x,f) 
        x = x + 1 
        y = (ry/rx)*np.sqrt((rx**2) - (x**2))
        f = int(y  + 0.5)
    y = 0 
    x = rx
    f = rx
    while (ry**2)*f >= (rx**2)*y:
        mat = fourPoitns(mat,p,x,f)
        y = y + 1
        x = (ry/rx)*np.sqrt(ry**2 - y**2)
        f = int(x + 0.5)
    return mat
