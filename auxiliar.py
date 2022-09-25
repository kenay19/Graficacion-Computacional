import cv2 as c
def graficmatriz(mat,name):
    c.imshow(name,mat[::-1])
    c.waitKey(0)
    c.destroyAllWindows()

divisor = 2 

def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a


def minimo_comun_multiplo(a, b):
    return (a * b) / maximo_comun_divisor(a, b)