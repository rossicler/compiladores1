import re
import os
import sys

class Lexico(object):
    def __init__(self):        
        self.tokens = []
        self.reserved_words = [
            'program','input','output',',','(',')',
            ';','var','integer','begin','end','.','read',
            ':=','>','>=','<','<=','<>',':','while','do',
            '+', '-', 'write', 'read'
        ]
        self.my_file_list = []
        

    def build(self):        
        with open(sys.argv[1], 'r') as my_file:
            self.my_file_list = my_file.read().split("\n")
        cont = 0

        texts = ""
        for line in self.my_file_list:
            texts += line + " "
        
        simbols = ["(", ">=", "<=", "<>", ">", "<", ",", ")", ";", ":=", "+", "-", '.', ':']

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
            elif simbol is ":":
                num = texts.count(simbol)
                for index in range(0, num):
                    position = texts.find(simbol)
                    if not (texts[position+1] == "="):
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


    def get_token_head(self):
        head, *tail = self.tokens
        self.tokens = tail
        return head

    
    def print_tokens(self):
        for token in self.tokens:
            print(token)

prog = Lexico()
prog.build()
prog.print_tokens()