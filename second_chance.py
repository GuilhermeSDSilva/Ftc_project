import string

# global variables
turing_machine = {}
delta = []
words = []
instructions = []
alphabet = {'x', '#', 'b'}  # only tape's alphabet
moviments = ['D', 'E', 'P']
head = 0
checking = True
cont = 0  # auxiliary counter
final_string = ''

# states
initial = input('')
accepted = input('')
rejected = input('')
current = initial

# filling the list delta with instructions
num_instructions = int(input(''))
for i in range(0, num_instructions):
    x = input('')
    instructions.append(x)
    y = input('')
    instructions.append(y)
    u = input('').lower()
    instructions.append(u)
    v = input('').lower()
    instructions.append(v)
    w = input('').upper()
    instructions.append(w)
    delta.append(tuple(instructions))
    instructions.clear()

# turing_machine = {'inicial': initial, 'aceita': accepted, 'rejeita': rejected, 'delta': delta}
words_number = int(input(""))
for i in range(0, words_number):
    word = input('')
    while head <= len(word):
        print(f'Estado: {current}, cabeçote: {head}, instrução: {cont}, resultado: {final_string}')
        print()
        if word[head] == delta[cont][2] and current == delta[cont][0]:
            current = delta[cont][1]
            final_string = final_string + delta[cont][3]
            cont = 0
            head = head + 1
        if delta[cont][3] in alphabet and current == delta[cont][0] and head >= len(word):
            current = delta[cont][1]
            if delta[cont][4] == 'P':
                if current == accepted:
                    print(f'{final_string} ACEITA')
                elif current == rejected:
                    print(f'{final_string} REJEITA')
            elif delta[cont][4] == 'D':
                head = head + 1
            elif delta[cont][4] == 'E':
                head = head - 1
        if cont >= num_instructions - 1:
            cont = 0
        else:
            cont = cont + 1
        if head >= len(word):
            for j in delta:
                if j[3] in alphabet:
                    current = j[1]
                    alpha = j[3]
                    print(alpha)
                    if j[4] == 'P':
                        if current == accepted:
                            print(f'{final_string} ACEITA')
                            break
                        elif current == rejected:
                            print(f'{final_string} REJEITA')
                            break
    head = 0
    cont = 0
    final_string = ''
