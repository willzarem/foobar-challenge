from fractions import Fraction, gcd
from pprint import pprint

def answer(m):
    if len(m) <= 1:
        return [1,1]
    mat = MarkovMatrix(m)
    mat.sustract(mat.I, mat.Q)
    mat.inverse(mat.result)
    mat.multiply(mat.result, mat.R)
    return mat.gtc(mat.result[0])

class MarkovMatrix:
    def __init__(self, matrix):
        self.matrix = []
        self.I = []
        self.R = []
        self.Q = []
        self.terminal_states = []
        self.result = []
        tmp = []
        for i,iv in enumerate(reversed(matrix[1::])):
            c = sum(iv)
            if c != 0:
                tmp = [iv] + tmp
            else:
                tmp = tmp + [iv]
        tmp = [matrix[0]] + tmp

        for i, iv in enumerate(tmp):
            c = sum(iv)
            self.matrix.append([])
            for j, jv in enumerate(iv):
                if c > 0:
                    if jv == 0:
                        self.matrix[i].append(0)
                    else:
                        self.matrix[i].append(Fraction(jv, c))
                else:
                    self.matrix[i].append(int(i == j))
            if c == 0:
                self.terminal_states.append(i)
              
        matrix_length_difference = int(len(self.matrix) - len(self.terminal_states))
        self.Q = [row[:matrix_length_difference] for row in self.matrix[:matrix_length_difference]]
        self.R = [row[matrix_length_difference:] for row in self.matrix[:matrix_length_difference]]
        for i in range(len(self.Q)):
            self.I.append([])
            for j in range(len(self.Q)):
                self.I[i].append(int(i == j))

    def sustract(self, m1, m2):
        result = []
        for i, iv in enumerate(m1):
            result.append([])
            for j, jv in enumerate(iv):
                result[i].append(jv - m2[i][j])
        self.result = result

    def inverse(self, matrix):
        if len(matrix) == 1:
            self.result = [[matrix[0][0]]]
        else:
            self.result = MatrixInverse().getMatrixInverse(matrix)

    def multiply(self, m1, m2):
        """Matrix multiplication function. Taken from: http://stackoverflow.com/a/39881495"""
        result = []
        for i in range(len(m1)): #for each row of m1
            row = m1[i]
            newRow = []
            for j in range(len(m2[0])): #for each column of m2
                y = 0
                for x in range(len(row)):
                    rowEl = row[x]
                    colEl = m2[x][j]
                    y += rowEl*colEl
                newRow.append(y)
            result.append(newRow)
        self.result = result

    def gtc(self, arr):
        bck = []
        res = Fraction(arr[0]).denominator
        for x in arr[1::]:
            res = self.lcm(res, Fraction(x).denominator)
        for x in arr:
            bck.append(res / Fraction(x).denominator * Fraction(x).numerator)
        bck.append(res)
        return bck
    def lcm(self, a, b):
        """Compute the lowest common multiple of a and b"""
        return a * b / gcd(a, b)

class MatrixInverse:
    """Collection of methods to inverse a matrix. Taken from this answer: http://stackoverflow.com/a/39881366"""
    def transposeMatrix(self, m):
        t = []
        for r in range(len(m)):
            tRow = []
            for c in range(len(m[r])):
                if c == r:
                    tRow.append(m[r][c])
                else:
                    tRow.append(m[c][r])
            t.append(tRow)
        return t

    def getMatrixMinor(self, m,i,j):
        return [row[:j] + row[j+1:] for row in m[:i]+m[i+1:]]

    def getMatrixDeternminant(self, m):
        #base case for 2x2 matrix
        if len(m) == 1:
            return m
        if len(m) == 2:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]

        determinant = 0
        for c in range(len(m)):
            determinant += ((-1)**c)*m[0][c]*self.getMatrixDeternminant(self.getMatrixMinor(m, 0, c))
        return determinant

    def getMatrixInverse(self, m):
        determinant = self.getMatrixDeternminant(m)

        if determinant == 0:
            return m

        if len(m) == 1:
            return m[0][0]
        #special case for 2x2 matrix:
        if len(m) == 2:
            return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                    [-1*m[1][0]/determinant, m[0][0]/determinant]]

        #find matrix of cofactors
        cofactors = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = self.getMatrixMinor(m, r, c)
                cofactorRow.append(((-1)**(r+c)) * self.getMatrixDeternminant(minor))
            cofactors.append(cofactorRow)
        cofactors = self.transposeMatrix(cofactors)
        for r in range(len(cofactors)):
            for c in range(len(cofactors)):
                cofactors[r][c] = cofactors[r][c]/determinant
        return cofactors

print(answer([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
print(answer([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
print(answer([[0, 1, 0, 1, 0], [2, 0, 1, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
print(answer([[1,1], [0,0]]))
