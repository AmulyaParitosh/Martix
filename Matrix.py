from __future__ import annotations
from copy import deepcopy
from math import isclose


class Matrix:
    matrix = []

    def __init__(self, mat=[]):
        self.matrix = mat

    @classmethod
    def oforder(cls, rows, columns, element=0,):
        matrix = [[float(element) for y in range(columns)]
                  for x in range(rows)]
        return cls(matrix)

    @classmethod
    def fromfile(cls, fname: str, which=0):
        File = open(fname, 'r')
        file = File.read()
        File.close()

        mat = file.split("\n\n")

        for m in range(len(mat)):
            mat[m] = mat[m].split("\n")
            for e in range(len(mat[m])):
                mat[m][e] = mat[m][e].split(" ")

        matrix = []
        temp_m = []
        temp_r = []

        # n = len(mat)
        # for i in range(n):

        i = which

        num_r = len(mat[i])
        for r in range(num_r):

            num_e = len(mat[i][r])
            for e in range(num_e):
                temp_r.append(float(mat[i][r][e]))

            temp_m.append(temp_r)
            temp_r = []

        matrix.append(temp_m)
        temp_m = []
        return cls(matrix[0])

    def __str__(Mat: Matrix):
        for m in Mat.matrix:
            print(m)

        return "\0"

    def eq_order(self, a: Matrix, b: Matrix) -> bool:

        n1, m1 = len(a.matrix), len(a.matrix[0])
        n2, m2 = len(b.matrix), len(b.matrix[0])

        return (n1 == n2) & (m1 == m2)

    def zeros(self, m, n) -> Matrix:
        matrix = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(0.)
            matrix.append(temp)

        return Matrix(matrix)

    def unit_matrix(self, n) -> Matrix:
        matrix = []
        for i in range(n):
            temp = []
            for j in range(n):
                if(i == j):
                    temp.append(1.)
                else:
                    temp.append(0.)
            matrix.append(temp)

        return Matrix(matrix)

    def __eq__(self, Mat2: Matrix) -> bool:
        if self.eq_order(self, Mat2):
            for x, y in list(zip(self.matrix, Mat2.matrix)):
                for p, q in list(zip(x, y)):
                    if not isclose(p, q):
                        return False
            return True
        else:
            return False

    def __add__(self, Mat2: Matrix) -> Matrix:

        a = self.matrix
        b = Mat2.matrix

        if(self.eq_order(a=self, b=Mat2)):

            n1, m1 = len(a), len(a[0])

            res = self.zeros(n1, m1)
            c = res.matrix

            for i in range(n1):
                for e in range(m1):
                    c[i][e] += a[i][e]+b[i][e]

            return res

        else:
            raise Exception(
                "Number of rows and columns of A & B are different")

    def __sub__(self, Mat2: Matrix) -> Matrix:
        a = self.matrix
        b = Mat2.matrix

        if(self.eq_order(a=self, b=Mat2)):

            n1, m1 = len(a), len(a[0])

            res = self.zeros(n1, m1)
            c = res.matrix

            for i in range(n1):
                for e in range(m1):
                    c[i][e] += a[i][e]-b[i][e]

            return res

        else:
            raise Exception(
                "Number of rows and columns of A & B are different")

    def __mul__(self, mat) -> Matrix:

        if not isinstance(mat, int):

            a = self.matrix
            b = mat.matrix

            n1, m1 = len(a), len(a[0])
            n2, m2 = len(b), len(b[0])

            if(n1 == m2 & n2 == m1):
                res = self.zeros(n1, m1)
                c = res.matrix
                temp = 0

                for i in range(n1):
                    for e in range(m2):
                        for j in range(m2):
                            temp += a[i][j]*b[j][e]

                        c[i][e] += temp
                        temp = 0

                return res
            else:
                raise Exception("Matrices not compatible for multiplication")

        else:
            res = self.zeros(len(self.matrix), len(self.matrix[0]))
            c = res.matrix

            for i in range(len(c)):
                for j in range(len(c[0])):
                    c[i][j] += self.matrix[i][j]*mat

            return res

    def __pow__(self, power) -> Matrix:

        x = len(self.matrix)
        res = self.unit_matrix(x)

        for i in range(power):
            res = res*self

        return res

    def __invert__(self) -> Matrix:
        matrix = deepcopy(self).matrix
        sz = len(matrix)
        szc = len(matrix[0])

        if(sz == szc):
            res = self.unit_matrix(sz)
            I = res.matrix

            for i in range(sz-1):
                for j in range(i+1, sz):
                    if(matrix[i][i] != 0):
                        x = matrix[j][i]/matrix[i][i]
                    for e in range(sz):
                        matrix[j][e] -= matrix[i][e]*x
                        I[j][e] -= I[i][e]*x

            for i in range(sz):
                x = matrix[i][i]
                for j in range(sz):
                    if x != 0:
                        matrix[i][j] /= x
                        I[i][j] /= x

            for i in range(sz-1, -1, -1):
                for j in range(i-1, -1, -1):
                    if(matrix[i][i] != 0):
                        x = matrix[j][i]/matrix[i][i]
                    for e in range(sz):
                        matrix[j][e] -= matrix[i][e]*x
                        I[j][e] -= I[i][e]*x

            return res

        else:
            raise Exception("Not a square Matrix!")

    def det(self) -> int:
        matrix = deepcopy(self).matrix
        n, m = len(matrix), len(matrix[0])
        det, temp = 0, 1
        x = 0

        if(n == m):

            if n == 2:
                det = matrix[0][0]*matrix[1][1]-matrix[1][0]*matrix[0][1]
                return det
            else:
                for i in range(n):
                    for j in range(n):
                        temp *= matrix[j][(j+i) % n]
                    det += temp
                    temp = 1

                for i in range(n):
                    for j in range(n-1, -1, -1):
                        x = matrix[n-j-1][(j+i) % n]
                        temp *= x
                    det -= temp
                    temp = 1

                return det

        else:
            raise Exception("Given matrix is not a square matrix")

    def rank(self) -> int:
        rank = 0
        matrix = deepcopy(self).matrix

        for i in range(len(matrix)-1):

            for j in range(i+1, len(matrix)):

                if(matrix[i][i] != 0):
                    x = matrix[j][i]/matrix[i][i]
                else:
                    x = 0

                for e in range(len(matrix[i])):
                    matrix[j][e] -= matrix[i][e]*x

        for row in matrix:
            for e in row:
                if(e != 0):
                    rank += 1
                    break

        return rank

    def add_row(self, row: list, pos):

        self.matrix.insert(pos, row)

    def add_column(self, row: list, pos):

        for i in range(len(self.matrix)):
            self.matrix[i].insert(pos, row[i])

    def transpose(self):

        sz = len(self.matrix)

        for i in range(sz):
            for j in range(i):
                temp = self.matrix[i][j]
                self.matrix[i][j] = self.matrix[j][i]
                self.matrix[j][i] = temp


if __name__ == "__main__":
    mat1 = Matrix.fromfile("input_file.txt", which=1)
    mat2 = Matrix.oforder(2, 2, 2)
    mat3 = Matrix([[1., 2.], [2., 1.]])
    print(mat1**2)
    print(~mat3)
    print(mat1)
