# EQUIPE: RAFAEL, GUILHERME, EMANUEL

# global variables
delta = []
words = []
instructions = []
head = 0
cont = 0
final_string = ''

# states
initial = input()
accepted = input()
rejected = input()
num_instructions = int(input())
current = initial

for i in range(0, num_instructions):
    x = input()
    instructions.append(x)
    y = input()
    instructions.append(y)
    u = input().lower()
    instructions.append(u)
    v = input().lower()
    instructions.append(v)
    w = input().upper()
    instructions.append(w)
    delta.append(tuple(instructions))
    instructions.clear()

words_number = int(input())
for i in range(0, words_number):
    word = input()
    while head < len(word):
        if (word[head] == delta[cont][2] and current == delta[cont][0]) or word[head] == delta[cont][2]:
            current = delta[cont][1]
            final_string = final_string + delta[cont][3]
            head = head + 1
        if cont >= num_instructions - 1:
            cont = 0
        else:
            cont = cont + 1
        if head >= len(word) and final_string.find('b') == -1:
            final_string = final_string + 'b'
            current = delta[cont][1]
            if current == accepted:
                print(current)
                print(f'{final_string} ACEITA')
            elif current != accepted:
                print(current)
                print(f'{final_string} REJEITA')
            head = 0
            cont = 0
            break
    while final_string.find('b') != -1:
        if final_string[head] == delta[cont][2] and current == delta[cont][0]:
            current = delta[cont][1]
            final_string.replace(final_string[head], delta[cont][3], 1)
            head = head + 1
        if cont >= num_instructions - 1:
            cont = 0
        else:
            cont = cont + 1
        if head >= len(final_string):
            current = delta[cont][1]
        if current == accepted:
            print(f'{final_string.replace('b', '')} ACEITA')
            break
        elif current == rejected:
            print(f'{final_string.replace('b', '')} REJEITA')
            break

    head = 0
    cont = 0
    current = initial
    final_string = ''
