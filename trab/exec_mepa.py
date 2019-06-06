import sys

class ExecMEPA():
    def __init__(self):
        self.D = []
        self.M = []
        self.s = -1
        self.i = 0
        self.my_file_list = []
        self.labels = {}
        self.n_param = [
            # 0 params
            [
                "SOMA", "SUBT", "MULT", "DIVI",
                "INVR", "CONJ", "DISJ", "NEGA",
                "CMME", "CMMA", "CMIG", "CMDG",
                "CMEG", "CMAG", "NADA", "PARA",
                "LEIT", "IMPR", "INPP"
            ],
            # 1 param
            [
                "DSVS", "DSVF", "AMEM", "DMEM",
                "ENPR", "CRCT"
            ],
            # 2 params
            [
                "CRVL", "CREN", "ARMZ",
                "CRVI", "ARMI", "ENRT", "CHPR",
                "RTPR"
            ],
            # 3 params
            [
                "DSVR"
            ]
        ]

    
    def main(self):
        with open(sys.argv[1], 'r') as my_file:
            self.my_file_list = my_file.read().split("\n")
            self.my_file_list = list(filter(None, self.my_file_list))
        self.__save_all_labels()
        
        self.__init_mem()
        instruction = ""
        while instruction != "PARA":
            line = self.my_file_list[self.i].strip()
            instruction = self.__get_instruction_string(self.my_file_list[self.i])
            self.__execute_instruction(instruction, line)
            self.__check_underflow()
            self.i += 1


    def __init_mem(self):
        for index in range(0, 1000):
            self.M.append(0)
            self.D.append(0)

    
    def __save_all_labels(self):
        for index, line in enumerate(self.my_file_list):
            position = line.find(":")
            if position != -1:
                line = line.strip()
                label = line[:position]
                self.labels[label] = index
                self.my_file_list[index] = line[position+1:]
        

    def __execute_instruction(self, instruction, line):
        if instruction in self.n_param[0]:
            func = getattr(self, instruction)
            func()
        elif instruction in self.n_param[1]:
            position = line.find(" ")
            param_1 = line[position:]
            param_1 = param_1.strip()
            func = getattr(self, instruction)
            if param_1.isdigit():
                param_1 = int(param_1)
            func(param_1)
        elif instruction in self.n_param[2]:
            position = line.find(" ")
            params = line[position:]
            params = params.split(",")
            params = [param.strip() for param in params]
            func = getattr(self, instruction)
            if params[0].isdigit():
                params[0] = int(params[0])
            func(params[0], int(params[1]))
        elif instruction in self.n_param[3]:
            position = line.find(" ")
            params = line[position:]
            params = params.split(",")
            params = [param.strip() for param in params]
            func = getattr(self, instruction)
            func(int(params[0]), int(params[1]), int(params[2]))


    def __get_instruction_string(self, line):
        instruction = line.strip()
        space_position = instruction.find(" ")
        if space_position != -1:
            instruction = instruction[:space_position]
        return instruction


    def __get_label_value(self, label):
        try:
            value = self.labels[label]
            return value
        except:
            error_msg = "Linha " + str(self.i + 1) + ": RunTime error rotulo " \
                + label + " invalido"
            print(error_msg)
            exit()


    def __check_underflow(self):
        if self.s < -1:
            error_msg = "Linha " + str(self.i+1) + ": RunTime error. Stack underflow"
            print(error_msg)
            exit()


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
        self.M[self.s - 1] = int(self.M[self.s - 1]) + int(self.M[self.s])
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
        self.i = self.__get_label_value(p)


    def DSVF(self, p):
        label = self.__get_label_value(p)
        if self.M[self.s] == 0:
            self.i = label
        else:
            pass
        self.s -= 1

    
    def NADA(self):
        pass


    def PARA(self):
        exit()


    def LEIT(self):
        self.s = self.s + 1
        self.M[self.s] = int(input())


    def IMPR(self):
        print(self.M[self.s])
        self.s -= 1


    def AMEM(self, n):
        self.s += n


    def DMEM(self, n):
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
        self.i = self.__get_label_value(p)


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
        self.i = self.__get_label_value(p)

prog = ExecMEPA()
prog.main()