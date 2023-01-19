print("""
Крестики-нолики
Игроки X и O вводят по очереди цифры от 1 до 9
Начало игры
""")

grid = list(range(1, 10))


def create_tabl(grid):
    print("#" * 13)
    for i in range(3):
        print("#", grid[0 + i * 3], "#", grid[1 + i * 3], "#", grid[2 + i * 3], "#")
        print("#" * 13)


def check(number):
    valid = False
    while not valid:
        answer = input("Введите целое число от 1 до 9. Игрок" + number + "?")
        try:
            answer = int(answer)
        except:
            print("Error. Введите целое число от 1 до 9?")
            continue
        if 1 <= answer <= 9:
            if str(grid[answer - 1]) not in "XO":
                grid[answer - 1] = number
                valid = True
            else:
                print("Такой ход уже был. Сделайте другой ход")
        else:
            print("Error. Введите целое число от 1 до 9.")


def Win(grid):
    win_cod = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_cod:
        if grid[each[0]] == grid[each[1]] == grid[each[2]]:
            return grid[each[0]]
    return False


def run(grid):
    counter = 0
    win = False
    while not win:
        create_tabl(grid)
        if counter % 2 == 0:
            check("X")
        else:
            check("O")
        counter += 1
        if counter > 4:
            fin = Win(grid)
            if fin:
                print(fin, "игрок победил")
                win = True
                break
        if counter == 9:
            print("ничья")
            break
    create_tabl(grid)


run(grid)
