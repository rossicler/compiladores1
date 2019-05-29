class ExecMEPA():
    def __init__(self):
        self.D = []
        self.M = []
        self.s = -1
        self.i = 0

    
    def main(self):
        print("AAAAAA")


    def CRCT(self, k):
        self.s += 1
        self.M[self.s] = k


    def CRVL(self, m, n):
        self.s += 1
        self.M[self.s] = self.M[self.D[m]+n]


    def CREN(self, m, n):
        self.s += 1
        self.M[self.s] = self.D[m] + n


    def ARMZ(self, m, n):
        self.M[self.D[m] + n] = self.M[self.s]
        self.s -= 1


    def CRVI(self, m, n):
        self.s += 1
        self.M[self.s] = self.M[self.M[self.D[m] + n]]

    
    def ARMI(self, m, n):
        self.M[self.M[self.D[m] + n]] = self.M[self.s]
        self.s -= 1


    def SOMA(self):
        self.M[self.s - 1] = self.M[self.s - 1] + self.M[self.s]
        self.s -= 1

    
    def SUBT(self):
        self.M[self.s - 1] = self.M[self.s - 1] - self.M[self.s]
        self.s -= 1


    def MULT(self):
        self.M[self.s - 1] = self.M[self.s - 1] * self.M[self.s]
        self.s -= 1


    def DIVI(self):
        self.M[self.s - 1] = self.M[self.s - 1] / self.M[self.s]
        self.s -= 1


    def INVR(self):
        self.M[self.s] = -self.M[self.s]


    def CONJ(self):
        if self.M[self.s - 1] == 1 and self.M[self.s] == 1:
            self.M[self.s - 1] = 1
        else:
            self.M[self.s - 1] = 0
        self.s -= 1

    
    def DISJ(self):
        if self.M[self.s - 1] == 1 or self.M[self.s] == 1:
            self.M[self.s - 1] = 1
        else:
            self.M[self.s - 1] = 0
        self.s -= 1


    def NEGA(self):
        self.M[self.s] = 1 - self.M[self.s]


    def CMME(self):
        if self.M[self.s - 1] < self.M[self.s]:
            self.M[self.s - 1] = 1
        else:
            self.M[self.s - 1] = 0
        self.s -= 1


    def CMMA(self):
        if self.M[self.s - 1] > self.M[self.s]:
            self.M[self.s - 1] = 1
        else:
            self.M[self.s - 1] = 0
        self.s -= 1


    def CMIG(self):
        if self.M[self.s - 1] == self.M[self.s]:
            self.M[self.s - 1] = 1
        else:
            self.M[self.s - 1] = 0
        self.s -= 1


    def CMDG(self):
        if self.M[self.s - 1] != self.M[self.s]:
            self.M[self.s - 1] = 1
        else:
            self.M[self.s - 1] = 0
        self.s -= 1


    def CMEG(self):
        if self.M[self.s - 1] <= self.M[self.s]:
            self.M[self.s - 1] = 1
        else:
            self.M[self.s - 1] = 0
        self.s -= 1


    def CMAG(self):
        if self.M[self.s - 1] >= self.M[self.s]:
            self.M[self.s - 1] = 1
        else:
            self.M[self.s - 1] = 0
        self.s -= 1


    def DSVS(self, p):
        self.i = p


    def DSVF(self, p):
        if self.M[self.s] == 0:
            self.i = p
        else:
            self.i += 1
        self.s -= 1

    
    def NADA():
        pass


    def PARA():
        exit()


    def LEIT(self):
        self.s = self.s + 1
        self.M[self.s] = input()


    def IMPR(self):
        print(self.M[self.s])
        self.s -= 1


    def AMEM(self, n):
        self.s += n


    def DMEN(self, n):
        self.s -= n

    
    def INPP(self):
        self.s = -1
        self.D[0] = 0


    def ENRT(self, j, n):
        self.s = self.D[j] + n - 1


    def CHPR(self, p, m):
        self.M[self.s + 1] = self.i + 1
        self.M[self.s + 2] = m
        self.s = self.s + 2
        self.i = p


    def ENPR(self, k):
        self.s = self.s + 1
        self.M[self.s] = self.D[k]
        self.D[self.k] = self.s + 1


    def RTPR(self, k, n):
        self.D[k] = self.M[self.s]
        self.i = self.M[self.s - 2]
        self.s = self.s - (n+3)

    def DSVR(self, p, j, k):
        temp1 = k
        while temp1 != j:
            temp2 = self.M[self.D[temp1]-2]
            self.D[temp1] = self.M[self.D[temp1] - 1]
            temp1 = temp2
        self.i = p


prog = ExecMEPA()
prog.main()