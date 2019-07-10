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
        print(self.tokens)


class Sintatico(object):
    def __init__(self):
        self.lexico = []
        self.vars = []
        self.mepa = []
        self.commands = [
            'read',
            'write',
            'while',
            'begin'
        ]

    def main(self):
        self.lexico = Lexico()
        self.lexico.build()
        self.program()

    def program(self):
        token = self.lexico.get_token_head()
        if token['value'] != "program":
            self.print_error(token['value'], "program")

        self.read_label('program')

        token = self.lexico.get_token_head()
        if token['value'] != "(":
            self.print_error(token['value'], "(")

        self.read_label('program_arguments')

        token = self.lexico.get_token_head()
        while token['value'] != ')':
            if token['value'] != ',':
                self.print_error(token['value'], ",")
            self.read_label('program')
            token = self.lexico.get_token_head()

        token = self.lexico.get_token_head()
        if token['value'] != ';':
            self.print_error(token['value'], ";")
        self.mepa.append("INPP")
        self.block()
        token = self.lexico.get_token_head()
        if token['value'] != '.':
            self.print_error(token['value'], '.')
        self.mepa.append("PARA")
        # write the mepa array to a file
        print("Aceito")
        exit()

    def block(self, token=""):
        if not token:
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

    def var_function(self, token=""):
        if not token:
            token = self.lexico.get_token_head()
        var_labels = [token['value']]
        token = self.lexico.get_token_head()
        while token['value'] != ':':
            if token['value'] != ',':
                self.print_error(token['value'], ",")
            label = self.read_var_label()
            var_labels.append(label)
            token = self.lexico.get_token_head()
        token = self.lexico.get_token_head()
        if token['value'] != 'integer':
            self.print_error(token=token['value'])
        self.bulk_insert_labels(var_labels, 'integer')
        token = self.lexico.get_token_head()
        if token['value'] != ';':
            self.print_error(token['value'], ';')
        token = self.lexico.get_token_head()
        if token['cod'] == 'reserved_word':
            self.block(token)
        else:
            self.var_function(token)

    def procedure_function(self):
        pass

    def function_declaration(self):
        pass
    
    def begin_function(self):
        self.command_without_rotule_function()

    def command_without_rotule_function(self, token=""):
        if not token:
            token = self.lexico.get_token_head()
        if token['cod'] == 'reserved_word':
            if token['value'] == 'end':
                return
            elif token['value'] not in self.commands:
                self.print_error(token['value'])
            self.read_command_function(token)
        else:
            self.read_command_function(token)
            # do something
    
    def read_command_function(self, token):
        if token['cod'] == 'label':
            self.set_value_function(token)
        elif token['value'] == 'read':
            self.read_function()
        elif token['value'] == 'write':
            self.write_function()
        elif token['value'] == 'while':
            self.while_function()
        elif token['value'] == 'begin':
            self.begin_function()            
            token = self.lexico.get_token_head()
            if token['value'] != ';':
                self.print_error(token['value'], ';')
        else:
            self.print_error(token['value'])

    def read_function(self):
        token = self.lexico.get_token_head()
        if token['value'] != '(':
            self.print_error(token['value'], '(')
        token = self.lexico.get_token_head()
        self.check_if_label_exists(token['value'])
        token = self.lexico.get_token_head()
        if token['value'] != ')':
            self.print_error(token['value'], ')')
        token = self.lexico.get_token_head()
        if token['value'] != ';':
            self.print_error(token['value'], ';')
        # generate MEPA code to read the value
        self.command_without_rotule_function()

    def write_function(self):
        token = self.lexico.get_token_head()
        if token['value'] != '(':
            self.print_error(token['value'], '(')
        token = self.lexico.get_token_head()
        self.check_if_label_exists(token['value'])
        token = self.lexico.get_token_head()
        if token['value'] != ')':
            self.print_error(token['value'], ')')
        token = self.lexico.get_token_head()
        if token['value'] != ';':
            self.print_error(token['value'], ';')
        # generate MEPA code to write the value
        self.command_without_rotule_function()      

    def set_value_function(self, token):
        self.check_if_label_exists(token['value'])
        token = self.lexico.get_token_head()
        if token['value'] != ':=':
            self.print_error(token['value'], ':=')
        token = self.lexico.get_token_head()
        if token['cod'] != 'label':
            self.print_error(token['value'], "a label that isn't a reserved word")
        if not token['value'].isdigit():
            self.check_if_label_exists(token['value'])
        token = self.lexico.get_token_head()
        if token['value'] != ';':
            if not token['value'] in ['+', '-', 'or']:
                self.print_error(token['value'], "one of the following, [-, +, or]")
            token = self.lexico.get_token_head()
            if not token['value'].isdigit():
                self.check_if_label_exists(token['value'])
            token = self.lexico.get_token_head()
            if token['value'] != ';':
                self.command_without_rotule_function(token)
        # generate MEPA code to write the value
        self.command_without_rotule_function()

    def while_function(self):
        self.expression_function()
        token = self.lexico.get_token_head()
        if token['value'] != 'do':
            self.print_error(token['value'], "do")
        self.command_without_rotule_function()
        

    def expression_function(self):
        token = self.lexico.get_token_head()
        self.check_if_label_exists(token['value'])
        token = self.lexico.get_token_head()
        if not token['value'] in ['=', '<>', '<', '<=', '>=', '>']:
            self.print_error(token['value'], "a conditional reserved word")
        token = self.lexico.get_token_head()
        self.check_if_label_exists(token['value'])

    def type(self):
        pass

    def print_error(self, token, expected_token=""):
        self.lexico.print_tokens()
        if expected_token:
            print("Found an error next to '" + token + "' it was expected " + expected_token)
        else:
            print("Found an error next to '" + token + "' invalid token")
        exit()

    def print_error_label(self, token):
        print("Found an error next to '" + token + "' this label already exists")
        exit()

    def check_label(self, label):
        if label[0].isdigit():
            self.print_error(token['value'], "a valid label")
        for var in self.vars:
            if label == var['label']:
                self.print_error_label(label)

    def check_if_label_exists(self, label):
        exist = False
        for var in self.vars:
            if label == var['label']:
                exist = True
                break
        if not exist:
            self.print_error(label)

    def read_label(self, type):
        token = self.lexico.get_token_head()
        self.check_label(token['value'])
        self.vars.append({'label': token['value'], 'type': type})

    def read_var_label(self):
        token = self.lexico.get_token_head()
        self.check_label(token['value'])
        return token['value']

    def bulk_insert_labels(self, labels, type):
        for label in labels:
            self.check_label(label)
            self.vars.append({'label': label, 'type': type})
            # needs to generate MEPA of the label if integer

prog = Sintatico()
prog.main()