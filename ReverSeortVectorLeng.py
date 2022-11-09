from math import sqrt

class Vector:
    def __init__(self,x,y,x1,y1):
        self.x=x
        self.y=y
        self.x1 = x1
        self.y1 = y1
        print("Начало вектора (", self.x, ";", self.y, ")", "Конец вектора (", self.x1, ";",self.y1, ")")

    def length(self):
        return sqrt((self.x-self.x1)**2+(self.y-self.y1)**2)

print('введите количество рассматриваемых векторов')

n = input() #число векторов

my_vectors = [] #массив под координаты

for i in range(int(n)): #заполнение массива my_vectors координатами через цикл
    print(
        f"Введи координаты точек начала и конца {i + 1} вектора."
        f" По одной координате на строку. В порядке начало: (x,y) конец вектора: (x,y)")
    my_vectors.append(Vector(float(input()), float(input()), float(input()), float(input())))

my_vectors_lenghts = [] #массив под длины векторов
for my_vector in my_vectors: #заполнение массива my_vectors_lenghts длинами через цикл
    my_vectors_lenghts.append(my_vector.length())
print("Отсортированные длины векторов")
print(sorted(my_vectors_lenghts, reverse=True)) #сортировка в порядке убывания длин вектров