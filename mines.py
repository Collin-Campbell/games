import random
import time
import sys

def round(level):
    a = ['.....','.....','.....','.....','.....']
    b = ['.....','.....','.....','.....','.....']
    c = ['.....','.....','.....','.....','.....']
    d = ['.....','.....','.....','.....','.....']
    e = ['.....','.....','.....','.....','.....']

    row = [a, b, c, d, e]
    number = level

    acceptable_responses = []

    for letter in ['A','B','C','D','E']:
        for num in range(1,6):
            acceptable_responses.append(str(letter) + str(num))

    print('\n\n')
    print(('                         LVL {}').format(number))
    print('    -------------------------------------------------')
    print('   |         |         |         |         |         |')
    print(' A |         |         |         |         |         |')
    print('   |         |         |         |         |         |')
    print('    -------------------------------------------------')
    print('   |         |         |         |         |         |')
    print(' B |         |         |         |         |         |')
    print('   |         |         |         |         |         |')
    print('    -------------------------------------------------')
    print('   |         |         |         |         |         |')
    print(' C |         |         |         |         |         |')
    print('   |         |         |         |         |         |')
    print('    -------------------------------------------------')
    print('   |         |         |         |         |         |')
    print(' D |         |         |         |         |         |')
    print('   |         |         |         |         |         |')
    print('    -------------------------------------------------')
    print('   |         |         |         |         |         |')
    print(' E |         |         |         |         |         |')
    print('   |         |         |         |         |         |')
    print('    -------------------------------------------------')
    print('        1         2         3         4         5')

    answer = ''

    while answer not in acceptable_responses:
        answer = (input('\n\nPick a box:  ')).upper().strip() 

    for _ in range(level*2):
        random.choice(row)[random.randint(0,4)] = 'BOOM!'
    random.choice(row)[random.randint(0,4)] = '.....'

    print('\n\ttick...') 
    time.sleep(0.5)
    print('\n\ttick...') 
    time.sleep(0.5)
    print('\n\ttick...\n\n')
    time.sleep(1)

    print(('                         LVL {}').format(number))
    print('    -------------------------------------------------')
    print('   |         |         |         |         |         |')
    print((' A |  {}  |  {}  |  {}  |  {}  |  {}  |').format(a[0],a[1],a[2],a[3],a[4]))
    print('   |         |         |         |         |         |')
    print('    -------------------------------------------------')
    print('   |         |         |         |         |         |')
    print((' B |  {}  |  {}  |  {}  |  {}  |  {}  |').format(b[0],b[1],b[2],b[3],b[4]))
    print('   |         |         |         |         |         |')
    print('    -------------------------------------------------')
    print('   |         |         |         |         |         |')
    print((' C |  {}  |  {}  |  {}  |  {}  |  {}  |').format(c[0],c[1],c[2],c[3],c[4]))
    print('   |         |         |         |         |         |')
    print('    -------------------------------------------------')
    print('   |         |         |         |         |         |')
    print((' D |  {}  |  {}  |  {}  |  {}  |  {}  |').format(d[0],d[1],d[2],d[3],d[4]))
    print('   |         |         |         |         |         |')
    print('    -------------------------------------------------')
    print('   |         |         |         |         |         |')
    print((' E |  {}  |  {}  |  {}  |  {}  |  {}  |').format(e[0],e[1],e[2],e[3],e[4]))
    print('   |         |         |         |         |         |')
    print('    -------------------------------------------------')
    print('        1         2         3         4         5')

    box_letters = {'a':a,'b':b,'c':c,'d':d,'e':e}

    if (box_letters[answer.lower()[0]])[int(answer[1])-1] == 'BOOM!':
        sys.exit("\n\nOops... better luck next time!\n\n")
    else:
        print('\n\nWhew!\n\n')

    time.sleep(4)


if __name__ == '__main__':
    print('\n\nMake it through 10 levels to win the game... good luck!\n\n')
    time.sleep(2)
    print('Example of acceptable box choice = a1\n')
    time.sleep(2)
    for num in range(1,11):
        round(num)
    print('\n\nCongratulations! You beat every level!\n\n')
