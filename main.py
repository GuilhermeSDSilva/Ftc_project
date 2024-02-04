# global variables
turing_machine = {}
delta = []
words = []
instructions = []
alphabet = {'1', '0', 'x', '#', 'b'}
moviments = ['D', 'E', 'P']
head = ""
checking = True
cont = 0  # auxiliary counter

# states
initial = input("")
accepted = input("")
rejected = input("")
words_number = int(input(""))
current = initial

# filling the list words with... words :)
for i in range(0, words_number):
    word = input("")
    words.append(word)

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

#turing_machine = {'inicial': initial, 'aceita': accepted, 'rejeita': rejected, 'delta': delta}

for i in range(0, words_number):
    while checking:
        for j in range(0, len(words[i])):
            while cont < len(delta):
                if words[i][j] == delta[cont][2]:
                    head = delta[cont][4]
                    current = delta[cont][1]
                    print(words[i][j])
                    #verificar por que nao aceita essa atribuição, provavelmente porque é uma manipulação muito interna nas strings
                    words[i][j] = delta[cont][3]
                    if delta[cont][4] == 'P':
                        if current == accepted:
                            print(f'{int(words[i])} ACEITA')
                            checking = False
                        elif current == rejected:
                            print(f'{int(words[i])} REJEITA')
                            checking = False
                    elif head == 'D':
                        cont = cont + 1
                        continue
                    elif head == 'E':
                        cont = cont + 1
                        j = j - 1
                else:
                    cont = cont + 1
            cont = 0
            head = ""
    checking = True
    cont = 0
    head = ""
