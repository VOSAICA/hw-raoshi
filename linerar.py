import numpy as np
class matrix():
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
        return a

    def __add__(self, other):
        c = matrix([[0 for j in range(self.column)] for i in range(self.row)])
        for i in range(0, self.row):
            for j in range(0, self.column):
                c.array[i][j] = self.array[i][j] + other.array[i][j]
        return c



a = matrix([[1,2,3], [1, 2, 3]])
b = matrix([[1,2,3], [1, 2, 3]])
print(a + b)