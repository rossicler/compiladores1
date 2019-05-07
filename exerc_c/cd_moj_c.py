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
        self.initial_state = '0'
        self.final_states = ['2']


    def main(self):
        # Main function
        self.word = input()
        self.__read_word(self.initial_state, self.word, '')

    def __next_state(self, state, letter, stack):
        # Passa para o próximo estado
        # se todos os outros requisitos
        # da transição forem aceitos
        for transition in self.table_transition:
            if transition[0] == state and (transition[1] == letter or transition[1] in ['','?']) \
                and (transition[2] == stack[:len(stack) - 1] or transition[2] in ['?', '']):

                # letter = '' if there wasn't read any letter
                if transition[1] != '':
                    letter = ''

                if transition[2] == '?':
                    if len(stack) == 0:
                        stack += transition[3]
                        print('nil')
                        next_state = transition[4]
                        return next_state, stack, letter
                elif transition[2] == '':
                    stack += transition[3]
                    if len(stack) == 0:
                        print('nil')
                    else:
                        print(stack)
                    next_state = transition[4]
                    return next_state, stack, letter
                elif re.search(".*" + transition[2] + "&", stack) is not -1:
                    stack_position = len(stack) - len(transition[2]) -1
                    stack = stack[:stack_position]
                    stack += transition[3]
                    if len(stack) == 0:
                        print('nil')
                    else:
                        print(stack)
                    next_state = transition[4]
                    return next_state, stack, letter


    def __read_letter(self, word):
        # Le uma letra da entrada
        return word[1:]
    

    def __read_word(self, state_now, word, stack):
        #Recursive function to read a word
        next_state, stack, letter = self.__next_state(state_now, word[0], stack)

        import pdb; pdb.set_trace()

        if letter != '':
            word = self.__read_letter(word)
        if len(word) == 0:
            if len(stack) == 0:
                print("Aceito")
                exit()
        else: 
            self.__read_word(next_state, word, stack)



prog = Cd_mod_B()
prog.main()