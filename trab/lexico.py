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
        self.program()

    def program(self):
        token = self.lexico.get_token_head()
        if token['value'] != "program":
            self.print_error(token['value'], "program")

        self.read_label()

        token = self.lexico.get_token_head()
        if token['value'] != "(":
            self.print_error(token['value'], "(")

        self.read_label()

        token = self.lexico.get_token_head()
        while token['value'] != ')':
            if token['value'] != ',':
                self.print_error(token['value'], ",")
            self.read_label()
            token = self.lexico.get_token_head()

        token = self.lexico.get_token_head()
        if token['value'] != ';':
            self.print_error(token['value'], ";")
        self.mepa.append("INPP")
        import pdb; pdb.set_trace()

    def block(self):
        token = self.lexico.get_token_head()
        if token['value'] == "label":
            self.label_function()
        elif token['value'] == "type":
            self.type_function()
        elif token['value'] == "var":
            self.var_function()
        elif token['value'] == "procedure":
            self.procedure_function()
        elif token['value'] == "function":
            self.function_declaration()
        elif token['value'] == "begin":
            self.begin_function()
        else:
            self.print_error(token=token['value'])

    def label_function(self):
        pass

    def type_function(self):
        pass

    def var_function(self):
        token = self.lexico.get_token_head()
        while token['value'] != ':':
            if token['value'] != ',':
                self.print_error(token['value'], ",")
            self.read_label()
            token = self.lexico.get_token_head()
        token = self.lexico.get_token_head()
        if token['value'] != 'integer':
            self.print_error(token=token['value'])
        token = self.lexico.get_token_head()
        if token['value'] != ';':
            self.print_error(token['value'], ';')

    def procedure_function(self):
        pass

    def function_declaration(self):
        pass
    
    def begin_function(self):
        pass

    def type(self):

    def print_error(self, token, expected_token=""):
        if expected_token:
            print("Found an error next to " + token + " it was expected " + expected_token)
        else:
            print("Found an error next to " + token + "invalid token")
        exit()

    def print_error_label(self, token):
        print("Found an error next to " + token + " this label already exists")
        exit()

    def check_label(self, label):
        if label[0].isdigit():
            self.print_error(token['value'], "a valid label")
        if label in self.vars:
            self.print_error_label(label)

    def read_label(self):
        token = self.lexico.get_token_head()
        self.check_label(token['value'])
        self.vars.append(token['value'])


prog = Sintatico()
prog.main()