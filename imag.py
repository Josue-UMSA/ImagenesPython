# -*- coding: utf-8 -*-
"""
Created on Thu May 20 14:02:58 2021

@author: CEMGAR
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def bordes(imagen):
    M, N = imagen.shape
    #Roberts
    #Kh=([-1, 0], [0, 1])
    #Kv=([0, 1], [-1, 0])
    
    #   SOBEL
    #Kh=([-1, 0, 1], [-2, 0, 2], [-1, 0, 1])
    #Kv=([-1, -2, -1], [0, 0, 0], [1, 2, 1])
    #Prewit
    Kh=([-1, 0, 1], [-1, 0, 1], [-1, 0, 1])
    Kv=([-1, -1, -1], [0, 0, 0], [1, 1, 1])
    
    # 10 x 10
   #Kh=([-1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
   #     [-1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 1], )
   # Kv=([-1, -1, -1 -1, -1, -1 -1, -1, -1, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
   #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    x=0
    while(x < M):
        y=0
        while(y < N):
            sx=mulMatriz(imagen, x, y, Kh)
            sy=mulMatriz(imagen, x, y, Kv)
            
            gx=int(pow((1/(len(Kh)*len(Kv)))*sx,2))
            gy=int(pow((1/(len(Kh)*len(Kv)))*sy,2))
            g=int(pow((gx+gy),1/2))           
            imagen[x,y]=g
            y+=1
        x+=1
    plt.imshow(imagen,'gray')
    cv.imwrite('resultado.jpg', imagen)
            
def mulMatriz(imagen,x,y,mascara):
    s=0
    i=0
    l=len(mascara)
    while(i < l):
        j=0
        while(j < l):
            try:
                s+=imagen[x+i,y+j]*mascara[i][j]
            except:
                s+=0
            j+=1
        i+=1
    return s
        
img = cv.imread('lago.png',0)
img = img[600:800,720:920]
ret,img = cv.threshold(img,127,255,cv.THRESH_BINARY)
#cv.imshow('win',img)
bordes(img)