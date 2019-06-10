import re
import os
import sys

class Lexico(object):
    def __init__(self):
        self.p_stack = []
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
        
        simbols = ["(", ">=", "<=", "<>", ">", "<", ",", ")", ";", ":=", "+", "-", '.']

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


    def get_token_head(self):
        head, *tail = self.tokens
        self.tokens = tail
        return head

    
    def print_tokens(self):
        print(self.tokens)


class Sintatico(object):
    def __init__(self):
        self.lexico = []
        self.vars = []
        self.mepa = []

    def main(self):
        self.lexico = Lexico()
        self.lexico.build()

    def program(self):
        token = self.lexico.get_token_head()
        if token.value != "program":
            self.print_error(token.value, "program")

        self.read_label()

        token = self.lexico.get_token_head()
        if token.value != "(":
            self.print_error(token.value, "(")

        self.read_label()

        token = self.lexico.get_token_head()
        while token.value != ')':
            if token.value != ',':
                self.print_error(token.value, ",")
            self.read_label()
            token = self.lexico.get_token_head()

        token = self.lexico.get_token_head()
        if token.value != ';':
            self.print_error(token.value, ";")
        self.mepa.append("INPP")

    def print_error(self, token, expected_token):
        print("Found an error next to " + token + " it was expected " + expected_token)
        exit()

    def print_error_label(self, token):
        print("Found an error next to " + token + " this label already exists")
        exit()

    def check_label(self, label):
        if label[0].isdigit():
            self.print_error(token.value, "a valid label")
        if label in self.vars:
            self.print_error_label(label)

    def read_label(self):
        token = self.lexico.get_token_head()
        self.check_label(token.value)
        self.vars.append(token.value)


prog = Sintatico()
prog.main()