import re
import os

class Lexico(object):
    def __init__(self):
        self.p_stack = []
        self.tokens = []
        self.reserved_words = [
            'program','input','output',',','(',')',
            ';','var','integer','begin','end','.','read',
            ':=','>','>=','<','<=','<>',':','while','do'
        ]
        

    def main(self):
        # Main function
        texts = input()
        cont = 0
#        for index, character in enumerate(texts):
#            if character in ["(", ">", "<", ",", ")", ";"]:
#                texts = texts[:index+cont] + " " + texts[index+cont:]
#                cont += 1
#                texts = texts[:index+cont+1] + " " + texts[index+cont+1:]
#                cont += 1
        
        simbols = ["(", ">=", "<=", "<>", ">", "<", ",", ")", ";", ":="]

        for simbol in simbols:
            if simbol is ">":
                num = texts.count(simbol)
                for index in range(0, num):
                    position = texts.find(simbol)
                    if not (texts[position-1] == "<" or texts[position+1] == "="):
                        texts = texts[:position] + " " + texts[position:]
            elif simbol is "<":
                num = texts.count(simbol)
                for index in range(0, num):
                    position = texts.find(simbol)
                    if not (texts[position+1] == ">" or texts[position+1] == "="):
                        texts = texts[:position] + " " + texts[position:]
            else:
                texts = texts.replace(simbol, ' ' + simbol + ' ')

        texts = texts.split(" ")
        texts = list(filter(None, texts))
        
        for text in texts:
            if text in self.reserved_words:
                self.tokens.append({
                    'cod': 'reserved_word',
                    'value': text
                })
            else:
                self.tokens.append({
                    'cod': 'label',
                    'value': text
                })

        for obj in self.tokens:
            print(obj)


prog = Lexico()
prog.main()