import numpy as np


class Matrix():
    def __init__(self, array):
        self.array = array
        self.row = len(array)
        self.column = len(array[0])

    def __str__(self):
        a = "["
        for i in range(0, self.row):
            if i == 0:
                a += "["
            else:
                a += " ["
            for j in range(0, self.column):
                if j == self.column - 1:
                    a += str(self.array[i][j])
                else:
                    a += str(self.array[i][j]) + ", "
            if i == self.row - 1:
                a += ']'
            else:
                a += ']' + "\n"
        a += ']'
        return a + "\n"

    def __add__(self, other):
        c = Matrix([[0 for j in range(self.column)] for i in range(self.row)])
        for i in range(0, self.row):
            for j in range(0, self.column):
                c.array[i][j] = self.array[i][j] + other.array[i][j]
        return c

    def __sub__ (self, other):
        c = Matrix([[0 for j in range(self.column)] for i in range(self.row)])
        for i in range(0, self.row):
            for j in range(0, self.column):
                c.array[i][j] = self.array[i][j] - other.array[i][j]
        return c

    def __mul__ (self, other):
        c = Matrix([[0 for j in range(other.column)] for i in range(self.row)])
        for i in range(0, c.row):
            for j in range(0, c.column):
                c.array[i][j] = self.__mulEle(other, i, j)
        return c

    def __mulEle (self, other, i, j):
        ele = 0
        for k in range(0, self.column):
            for l in range(0, other.row):
                ele += self.array[i][k] * other.array[l][j]
        return ele



a = Matrix([[1,2], [5, 0]])
b = Matrix([[3, 4], [0, 2]])

#print(a + b)
#print(a - b)
print(a * b)

c = np.array([[1, 2, 3], [12, 3, 4]])
print(c)