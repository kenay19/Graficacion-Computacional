# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 16:25:31 2022

@author: omarl
"""
import cv2 as c

def lineBasic(mat,p1,p2):
    m = (p1[1]-p2[1])/(p1[0]-p2[0])
    for i in range(p1[0],p2[0],1):
        Y = m*(i-p1[0])+p1[1]
        mat[int(Y+0.5),i] = 255
    c.imshow('Line Basis',mat[::-1])
    c.waitKey(0)
    c.destroyAllWindows()

def incremental(mat,p1, p2):
    m = (p1[1]-p2[1])/(p1[0]-p2[0])
    y = p1[1]
    for x in range(p1[0],p2[0],1):
        mat[x,int(y+0.5)] = 255
        y = y + m 
    c.imshow('Line incremental',mat[::-1])
    c.waitKey(0)
    c.destroyAllWindows()

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
    c.imshow('Line DDA',mat[::-1])
    c.waitKey(0)
    c.destroyAllWindows()

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
    c.imshow('Line bresenham',mat[::-1])
    c.waitKey(0)
    c.destroyAllWindows()

