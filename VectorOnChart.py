import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

class Vector:
    def __init__(self,x,y,x1,y1): #создание объекта класса с определенными парметрами
        self.x=x
        self.y=y
        self.x1 = x1
        self.y1 = y1
        print("Вектор создан") #когда объект создан
        print("Начало вектора (", self.x, ";", self.y, ")", "Конец вектора (", self.x1, ";",self.y1, ")") #когда объект создан

    def length(self): #нахождение длины вектора
        print("Длина вектора")
        print(sqrt((self.x-self.x1)**2+(self.y-self.y1)**2)) #формула нахождения длины вектора

    def draw(self,v = 0, v2 = 0): #печать вектора
        v = np.array([self.x,self.y])
        v2 = np.array([self.x1,self.y1])
        plt.grid()
        plt.plot(v[0], v[1], 'o')
        plt.plot(v2[0], v2[1], '>')
        plt.xlim(0, 10)
        plt.ylim(0, 10)

        plt.plot([self.x, self.x1], [self.y, self.y1])

        plt.show()

print("Введи корденаты точек начала и конца вектора. По одной кооденате на строку. В порядке начало: (x,y) конец вектора: (x,y)")
my_Vector = Vector(float(input()), float(input()), float(input()), float(input())) #создание объкта класса
my_Vector.length()
my_Vector.draw()