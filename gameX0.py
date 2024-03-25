def greet():
    print("  Hello! ")
    print("Let's play ")
    print(" the game ")
    print("Tic Tac Toe! ")
    print("------------ ")
    print(" Input format ")
    print("We use numbers")
    print("in range 0, 1, 2")
    print(" a - string ")
    print(" b - column ")
    print("------------ ")
    print(" Good luck! ")

field = [[" "] * 3 for i in range(3)]
# print(field)

def show():
    print()
    print("     0 | 1 | 2 |")
    print(" ---------------")
    for i, row in enumerate(field):
        row_str=f" {i} | {' | '.join(row)} |"
        print(row_str)
        print(" ---------------")
    print()
# show()

def ask():
    while True:
        print("ATTENTION!")
        print("We use numbers in range 0, 1, 2")
        cords=input("Your turn  (a, b):").split()
        if len(cords) != 2:
            print("We need 2 numbers")
            continue
        a,b = cords
        if not(a.isdigit()) or not(b.isdigit()):
            print("Sorry, but we use only numbers")
            continue
        a,b = int(a), int(b)
        if 0<=a<=2 and 0<=b<=2:
            if field[a][b] == " ":
                return a, b
            else:
                print("Sorry u can't")
                print("The cage is occupied")
                continue
        else:
            print("Above the range!")
            continue
def win_check():
    win_combination = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cords in win_combination:
        symbol = []
        for c in cords:
            symbol.append(field[c[0]][c[1]])
        if symbol == ["X", "X", "X"]:
            print("X win!!")
            return True

        if symbol == ["0", "0", "0"]:
            print("0 win!!")
            return True
    return False



greet()
count=0
while True:
    show()
    count += 1
    if count % 2 == 1:
        print("Go 0")
    else:
        print("Go X")

    a,b=ask()

    if count % 2 == 1:
        field[a][b]= "0"
    else:
        field[a][b]= "X"

    if win_check():
        break

    if count == 9:
        print("friendship won!:)")
        break
