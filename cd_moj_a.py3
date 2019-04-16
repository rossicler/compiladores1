import re

class Cd_mod_A():    
    qt_state = input()
    alphabet_input = input()

    num_simbols = alphabet_input[:alphabet_input.find(" ")]
    alphabet_input = alphabet_input[alphabet_input.find(" ") + 1:]
    alphabet = []
    for index in range(0, int(num_simbols)):
        substring = alphabet_input.find(" ")
        if substring != -1:
            alphabet.append(alphabet_input[:substring])
        else:
            alphabet.append(alphabet_input)
        alphabet_input = alphabet_input[alphabet_input.find(" ") + 1:]

    table_transition = []
    for index_i in range(0, int(qt_state)):
        for index_j in range(0, int(num_simbols)):
            transition = input()

            initial_state = transition[:transition.find(" ")]
            transition = transition[transition.find(" ") + 1:]
            word = transition[:transition.find(" ")]
            final_state = transition[transition.find(" ") + 1:]

            transition_cell = [initial_state, word, final_state]
            table_transition.append(transition_cell)

    initial_state = input()

    final_states_input = input()
    num_final_states = final_states_input[:final_states_input.find(" ")]
    final_states_input = final_states_input[final_states_input.find(" ") + 1:]
    final_states = []
    for index in range(0, int(num_final_states)):
        substring = final_states_input.find(" ")
        if substring != -1:
            final_states.append(final_states_input[:substring])
        else:
            final_states.append(final_states_input)
        final_states_input = final_states_input[final_states_input.find(" ") + 1:]
    
    word = input()

    state = int(initial_state)
    for val in word:
        if val in alphabet:
            for transition in table_transition:
                if transition[0] == str(state) and transition[1] == val:
                    state = int(transition[2])
                    break
        else:
            print("Letra não reconhecida")
            exit()

    print("Aceito") if str(state) in final_states else print("Rejeito")
    
