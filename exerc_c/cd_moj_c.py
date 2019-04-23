import re
import os

class Cd_mod_B(object):
    def __init__(self):
        self.word = ""
        self.alphabet = ['a', 'b']
        # Legenda
        # [A, B, C, D, E]
        # A = estado atual
        # B = letra a ser lida
        # C = palavra a ser consumida da pilha
        # D = palavra a ser empilhada
        # E = proximo estado
        # ? = não possui mais nada a ser lido
        #   = vazio, não faz nada
        self.table_transition = [
            ['0', 'a', 'A', 'AA', '0'],
            ['0', 'a', '?', 'A', '0'],
            ['0', 'a', 'B', '', '0'],
            ['0', '', '', '', '1'],
            ['1', '', '', '', '0'],
            ['1', 'b', '?', 'B', '1'],
            ['1', 'b', 'A', '', '1'],
            ['1', 'b', 'B', 'BB', '1'],
            ['0', '?', '?', '', '2'],
            ['1', '?', '?', '', '2']
        ]
        self.final_states = ['2']
        self.pilha = ""


    def main(self):
        # Main function

    def __next_state(self, transition):
        # Passa para o próximo estado
        # se todos os outros requisitos
        # da transição forem aceitos

    def __le_letra(self, word):
        # Le uma letra da entrada
    
    def __consume_pilha(self, word):
        # Consume uma palavra da pilha

    def __empilha_pilha(self, word):
        # Empilha uma palavra na pilha


prog = Cd_mod_B()
prog.main()