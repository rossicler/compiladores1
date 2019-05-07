import re
import os

class Lexico(object):
    def __init__(self):
        self.p_stack = []
        self.tokens = []
        

    def main(self):
        # Main function
        texts = input()
        cont = 0
        for index, character in enumerate(texts):
            if character == "(":
                texts = texts[:index+1+cont] + " " + texts[index+1+cont:]
                cont += 1
                texts = texts[:index+cont] + " " + texts[index+cont:]
                cont += 1
            elif character == ")":
                texts = texts[:index+cont] + " " + texts[index+cont:]
                cont += 1
            elif character == ",":
                texts = texts[:index+cont] + " " + texts[index+cont:]
                cont += 1
            elif character == ";":
                texts = texts[:index+cont] + " " + texts[index+cont:]
                cont += 1

        texts = texts.split(" ")
        texts.remove('')

        for text in texts:
            print(text)
        # for index, text in enumerate(texts):
        #     for character in text:
        #         if character == "(":
                   # Put A in the p_stack for an open parenthesis
        #             self.p_stack.append("A")

        #         elif character == ")":
        #             if len(self.p_stack) == 0:
        #                 print("Rejeito, ')' inesperado")
        #                 exit()
        #             else:
        #                 # Delete the last 'A' in p_stack
        #                 self.p_stack = self.p_stack[:len(self.p_stack) - 1]


prog = Lexico()
prog.main()