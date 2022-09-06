import cv2 as c
def graficmatriz(mat,name):
    c.imshow(name,mat[::-1])
    c.waitKey(0)
    c.destroyAllWindows()