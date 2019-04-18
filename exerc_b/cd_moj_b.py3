import re
import os

class Cd_mod_B(object):
    def __init__(self):
        self.word = ""
        self.alphabet = []
        self.reached_states = []
        self.table_transition = []


    def __read_word(self, current_state, word_position):
        
        if self.word[word_position] in self.alphabet:
            for transition in self.table_transition:
                if transition[0] == str(current_state) and transition[1] == self.word[word_position]:
                    for next_state in transition[2]:
                        current_state = int(next_state)
                        if len(self.word) == word_position + 1:
                            if current_state not in self.reached_states:
                                self.reached_states.append(current_state)
                            continue
                        self.__read_word(current_state, word_position + 1)
        else:
            print("Letra não reconhecida")
            exit()

        return None

    def main(self):
        qt_state = input()
        alphabet_input = input()

        num_simbols = alphabet_input[:alphabet_input.find(" ")]
        alphabet_input = alphabet_input[alphabet_input.find(" ") + 1:]
        for index in range(0, int(num_simbols)):
            substring = alphabet_input.find(" ")
            if substring != -1:
                self.alphabet.append(alphabet_input[:substring])
            else:
                self.alphabet.append(alphabet_input)
            alphabet_input = alphabet_input[alphabet_input.find(" ") + 1:]

        for index_i in range(0, int(qt_state)):
            for index_j in range(0, int(num_simbols)):
                transition = input()

                initial_state = transition[:transition.find(" ")]
                transition = transition[transition.find(" ") + 1:]
                self.word = transition[:transition.find(" ")]
                transition = transition[transition.find(" ") + 1:]
                next_states = []
                if transition.find(" ") == -1:
                    num_next_states = transition
                else:
                    num_next_states = transition[:transition.find(" ")]
                    transition = transition[transition.find(" ") + 1:]
                    for index_state in range(0, int(num_next_states)):
                        if index_state >= int(num_next_states) - 1:
                            next_state = transition
                            next_states.append(int(next_state))
                            break
                        next_state = transition[:transition.find(" ")]
                        next_states.append(int(next_state))
                        transition = transition[transition.find(" ") + 1:]

                transition_cell = [initial_state, self.word, next_states]
                self.table_transition.append(transition_cell)

        initial_state = input()

        final_states_input = input()
        num_final_states = final_states_input[:final_states_input.find(" ")]
        final_states_input = final_states_input[final_states_input.find(" ") + 1:]
        final_states = []
        for index in range(0, int(num_final_states)):
            substring = final_states_input.find(" ")
            if substring != -1:
                final_states.append(int(final_states_input[:substring]))
            else:
                final_states.append(int(final_states_input))
            final_states_input = final_states_input[final_states_input.find(" ") + 1:]
        
        self.word = input()

        state = int(initial_state)
        # Chamar função recursiva
        self.__read_word(0, 0)
        
        print(self.reached_states)
        print(final_states)
        for reached_state in self.reached_states:
            if reached_state in final_states:
                print("Aceito")
                exit()
        print("Rejeito")


prog = Cd_mod_B()
prog.main()
    
