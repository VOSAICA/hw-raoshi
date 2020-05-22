import numpy as np


class Vector():
    def __init__(self, array):
        self.array = array
        self.row = len(array)
        self.column = -1

    def __str__(self):
        c = "["
        for i in range(self.row):
            if i == self.row - 1:
                c += " " + str(self.array[i])
            elif i == 0:
                c += str(self.array[i])
            else:
                c += " " + str(self.array[i])
        c += "]"
        return c

    def innerProd(self, other):
        c = 0
        for i in range(0, self.row):
            c += self.array[i] * other.array[i]
        return c

    def outerProd(self, other):
        c = Matrix([[0 for j in range(self.row)] for i in range(self.row)])
        for i in range(0, self.row):
            for j in range(0, self.row):
                c.array[i][j] = self.array[i] * other.array[j]
        return c


class Matrix():
    def __init__(self, array):
        self.array = array
        self.row = len(array)
        self.column = len(array[0])

    def __str__(self):

        maxlen = [0 for j in range(self.column)]
        for i in range(0, self.row):
            for j in range(0, self.column):
                if len(str(self.array[i][j])) > maxlen[j]:
                    maxlen[j] = len(str(self.array[i][j]))

        a = "["
        for i in range(0, self.row):
            if i == 0:
                a += "["
            else:
                a += " ["
            for j in range(0, self.column):
                extraspace = maxlen[j] - len(str(self.array[i][j]))
                if j == self.column - 1:
                    a += " " * extraspace + str(self.array[i][j])
                elif j == 0:
                    a += " " + " " * extraspace + str(self.array[i][j]) + "  "
                else:
                    a += " " * extraspace + str(self.array[i][j]) + "  "
            if i == self.row - 1:
                a += ']'
            else:
                a += ']' + "\n"
        a += ']'
        return a

    def __add__(self, other):
        c = Matrix([[0 for j in range(self.column)] for i in range(self.row)])
        for i in range(0, self.row):
            for j in range(0, self.column):
                c.array[i][j] = self.array[i][j] + other.array[i][j]
        return c

    def __sub__(self, other):
        c = Matrix([[0 for j in range(self.column)] for i in range(self.row)])
        for i in range(0, self.row):
            for j in range(0, self.column):
                c.array[i][j] = self.array[i][j] - other.array[i][j]
        return c

    def __mul__(self, other):
        if other.column == -1:
            c = Vector([1 for i in range(self.row)])
            for i in range(0, self.row):
                c.array[i] = self.__mulVec(other, i)
            return c
        else:
            c = Matrix([[0 for j in range(other.column)]
                        for i in range(self.row)])
            for i in range(0, c.row):
                for j in range(0, c.column):
                    c.array[i][j] = self.__mulEle(other, i, j)
            return c

    def __mulEle(self, other, i, j):
        ele = 0
        for k in range(0, self.column):
            ele += self.array[i][k] * other.array[k][j]
        return ele

    def __mulVec(self, other, i):
        ele = 0
        for k in range(0, self.column):
            ele += self.array[i][k] * other.array[k]
        return ele

    def eleWise(self, other):
        c = Matrix([[0 for j in range(self.column)] for i in range(self.row)])
        for i in range(0, self.row):
            for j in range(0, self.column):
                c.array[i][j] = self.array[i][j] * other.array[i][j]
        return c


a = Matrix([[1, 2, 5], [5, 0, 2], [1, 3, 4]])
b = Matrix([[3, 4, 1], [0, 2, 1], [2, 3, 7]])
c = Vector([2, 3, 1])
d = Vector([2, 4, 2])

print("Mine:\n")
print(a + b, "\n")
print(a - b, "\n")
print(a * b, "\n")
print(a * c, "\n")
print(Matrix.eleWise(a, b), "\n")
print(Vector.innerProd(c, d), "\n")
print(Vector.outerProd(c, d), "\n")
print("-----" * 20)

print("Numpy:\n")
a = np.array([[1, 2, 5], [5, 0, 2], [1, 3, 4]])
b = np.array([[3, 4, 1], [0, 2, 1], [2, 3, 7]])
c = np.array([2, 3, 1])
d = np.array([2, 4, 2])

print(a + b, "\n")
print(a - b, "\n")
print(np.matmul(a, b), "\n")
print(np.matmul(a, c), "\n")
print(a * b, "\n")
print(np.inner(c, d), "\n")
print(np.outer(c, d), "\n")
