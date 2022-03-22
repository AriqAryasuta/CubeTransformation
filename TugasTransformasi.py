from graphics import *
import numpy as np
from numpy.linalg import inv, multi_dot
from math import sin, cos, radians, sqrt

koor = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])


win = GraphWin("Cube", 1080, 1080)
m = np.zeros([4,8])
mt = np.zeros([4,8])
x = 0

def MatrixInput():
    for i in range(8):
        print("Masukkan titik koordinat masing masing kubus", koor[i] )
        m[3][i] = 1
        for j in range(3):
            m[j][i] = int(input())
    print(m)

def Cube(m, color):
    xline = Line(Point(0,405), Point(1080,675))
    xline.setFill('green')
    yline = Line(Point(0,1080), Point(1080,0))
    yline.setFill('blue')
    zline = Line(Point(540,0), Point(540,1080))
    zline.setFill('red')
    xline.draw(win)
    yline.draw(win)
    zline.draw(win)

    for i in range(len(m[0])):
      if i < 4:
          gKoor= Line(Point(540+(m[0][i]+(m[1][i]/2)),540-(m[2][i]+(m[1][i]-(m[0][i]/4)))), Point(540+(m[0][i+4]+(m[1][i+4]/2)),540-(m[2][i+4]+(m[1][i+4]-(m[0][i+4]/4)))))
          gKoor.setFill(color)
          gKoor.draw(win)
      if i != 3 and i !=7:
        gKoor = Line(Point(540+(m[0][i]+(m[1][i]/2)),540-(m[2][i]+(m[1][i]-(m[0][i]/4)))), Point(540+(m[0][i+1]+(m[1][i+1]/2)),540-(m[2][i+1]+(m[1][i+1]-(m[0][i+1]/4)))))
        gKoor.setFill(color)
        gKoor.draw(win)
        
      else:
        gKoor = Line(Point(540+(m[0][i]+(m[1][i]/2)),540-(m[2][i]+(m[1][i]-(m[0][i]/4)))), Point(540+(m[0][i-3]+(m[1][i-3]/2)),540-(m[2][i-3]+(m[1][i-3]-(m[0][i-3]/4)))))
        gKoor.setFill(color)
        gKoor.draw(win)


def Translasi(mt):
    global x
    print("Menu Translasi")
    tx = int(input("Masukkan nilai dari translasi X: "))
    ty = int(input("Masukkan nilai dari translasi Y: "))
    tz = int(input("Masukkan nilai dari translasi Z: "))
    
    tm = np.array([[1,0,0,tx],
                  [0,1,0,ty],
                  [0,0,1,tz],
                  [0,0,0,1]])
    if x == 0:
        z = np.dot(tm, m)
        x = 1
    elif x == 1:
        z = np.dot(tm, mt)
    print("Matrix Hasil transformasi \n")
    print(z)
    return(z)

def RotasiX(mt):
    global x
    sudut = radians(int(input("Masukkan nilai rotasi terhadap sumbu X: ")))
    sinR = sin(sudut)
    cosR = cos(sudut)
    rX = np.array([[1, 0, 0, 0],
                   [0, sinR, -(sinR), 0], 
                   [0,sinR, cosR, 0],
                   [0,0,0,1]])
    if x == 0:
        z = np.dot(rX, m)
        x = 1
    elif x == 1:
        z = np.dot(rX, mt)
    print("Matrix Hasil transformasi \n")
    print(z)
    return(z)

def RotasiY(mt):
    global x
    sudut = radians(int(input("Masukkan nilai rotasi terhadap sumbu Y: ")))
    sinR = sin(sudut)
    cosR = cos(sudut)
    rY = np.array([[cosR, 0, sinR, 0],
                   [0, 1, 0, 0], 
                   [-(sinR), 0, cosR, 0],
                   [0,0,0,1]])
    if x == 0:
        z = np.dot(rY, m)
        x = 1
    elif x == 1:
        z = np.dot(rY, mt)
    print("Matrix Hasil transformasi \n")
    print(z)
    return(z)

def RotasiZ(mt):
    global x
    sudut = radians(int(input("Masukkan nilai rotasi terhadap sumbu Z: ")))
    sinR = sin(sudut)
    cosR = cos(sudut)
    rZ = np.array([[cosR, -(sinR), 0, 0],
                   [sinR, cosR, 0, 0], 
                   [0, 0, 1, 0],
                   [0,0,0,1]])
    if x == 0:
        z = np.dot(rZ, m)
        x = 1
    elif x == 1:
        z = np.dot(rZ, mt)
    print("Matrix Hasil transformasi \n")
    print(z)
    return(z)

def RotasiBebas(mt):
    global x
    p1 = np.zeros([3])
    p2 = np.zeros([3])
    sudut = radians(int(input("Masukkan nilai sudut putar : ")))
    print("Masukkan nilai titik awal garis: ")
    for i in range(3):
        p1[i] = int(input())
    print("Masukkan nilai titik akhir garis: ")
    for i in range (3):
        p2[i] = int(input())
    pRot = np.array(p2-p1)
    L = sqrt(np.sum(np.power(pRot, 2)))
    V = sqrt((pRot[1] + pRot[2])**2)
    mRx = RX(L, V, pRot)
    mRy = RY(L, V, pRot)
    mRz = RZ(sudut)
    T = np.array([[1, 0, 0, -(p1[0])], [0, 1, 0, -(p1[1])], [0, 0, 1, -(p1[2])], [0, 0, 0, 1]])
    rotate = kalkulasi(mRx, mRy, mRz, T)
    if x == 0:
        z = np.dot(rotate, m)
        x = 1
    elif x == 1:
        z = np.dot(rotate, mt)
    
    print("Matrix Hasil transformasi \n")
    print(z)
    return(z)

def RX(L, V, P):
    m = np.array([[1, 0, 0, 0], [0, (P[2]/V), -(P[1]/V), 0], [0, (P[1]/V), (P[2]/V), 0], [0, 0, 0, 1]])
    return(m)

def RY(L, V, P):
    m = np.array([[(V/L), 0, -(P[0]/L), 0], [0, 1, 0, 0], [(P[0]/L), 0, (V/L), 0], [0, 0, 0, 1]])
    return(m)

def RZ(t):
    m = np.array([[cos(t), -(sin(t)), 0, 0],[sin(t), cos(t), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    return(m)

def kalkulasi(x, y, z, t):
    m = multi_dot([inv(t), inv(x), inv(y), z, y, x, t])
    return(m)

def Scaling(mt):
    global x
    print("Jika tidak ada nilai scaling terhadap sumbu tertentu input nilai 1")
    sX = int(input("Masukkan nilai scaling terhadap sumbu X: "))
    sY = int(input("Masukkan nilai scaling terhadap sumbu Y: "))
    sZ = int(input("Masukkan nilai scaling terhadap sumbu Z: "))
    sh = np.array([[sX, 0, 0, 0],[0, sY, 0, 0], [0, 0, sZ,0], [0, 0, 0, 1]])
    if x == 0:
        z = np.dot(sh, m)
        x = 1
    elif x == 1:
        z = np.dot(sh, mt)
    
    print("Matrix Hasil transformasi \n")
    print(z)
    return(z)

def Shearing(mt):
    global x
    print("Pilih opsi untuk Shearing \n 1 Shearing XY \n 2 Shearing XZ \n 3 Shearing YZ")
    plhn = int(input())
    if plhn == 1:
        shX = int(input(print("Masukkan input shearing X: ")))
        shY = int(input(print("Masukkan input shearing Y: ")))
        shXY = np.array([[1, 0, shX, 0], [0, 1, shY, 0], [0, 0, 1, 0],[0, 0, 0, 1]])
        if x == 0:
            z = np.dot(shXY, m)
            x = 1
        elif x == 1:
            z = np.dot(shXY, mt)
    elif plhn == 2:
        shX = int(input(print("Masukkan input shearing X: ")))
        shZ = int(input(print("Masukkan input shearing Z: ")))
        shXZ = np.array([[shX, 0, 0, 0], [0, 1, 0, 0], [shZ, 0, 1, 0],[0, 0, 0, 1]])
        if x == 0:
            z = np.dot(shXZ, m)
            x += 1
        elif x == 1:
            z = np.dot(shXZ, mt)
    elif plhn == 3:
        shY = int(input(print("Masukkan input shearing Y: ")))
        shZ = int(input(print("Masukkan input shearing Z: ")))
        shYZ = np.array([[1, 0, 0, 0], [0, shY, 0, 0], [0, shZ, 1, 0], [0, 0, 0, 1]])
        if x == 0:
            z = np.dot(shYZ, m)
            x = 1
        elif x == 1:
            z = np.dot(shYZ, mt)
    else :
        print("Input tidak valid")
        Shearing(x, mt)
    
    print("Matrix Hasil transformasi \n")
    print(z)
    return(z)

def Menu():
    global mt
    aMenu = True
    while aMenu == True:
        print("Pilih salah satu menu transformasi \n 1 Translation \n 2 Scaling \n 3 Shearing \n 4 Rotating \n 5 Selesai")
        plhn = int(input())
        if plhn == 1:
            mt = Translasi(mt)
        elif plhn == 2:
            mt = Scaling(mt)
        elif plhn == 3:
            mt = Shearing(mt)
        elif plhn == 4:
            opt = int(input("Pilih jenis rotasi \n 1 Rotasi sumbu x \n 2 Rotasi sumbu y \n 3 Rotasi sumbu z \n 4 Rotasi terhadap suatu garis "))
            if opt == 1:
                mt = RotasiX(mt)
            elif opt == 2:
                mt = RotasiY(mt)
            elif opt == 3:
                mt = RotasiZ(mt)
            elif opt == 4:
                mt = RotasiBebas(mt)
        elif plhn == 5:
            Cube(m, 'black')
            Cube(mt, 'orange')
            aMenu = False
        else:
            print("Input tidak valid")
            Menu()

MatrixInput()
Menu()
