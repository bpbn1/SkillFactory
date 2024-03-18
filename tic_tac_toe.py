board = [[' '] * 3 for i in range(3)]

print('\nДля выбора позиции выберите номер строки по\nвертикали и номер столбца по горизонтали.'
          '\n\t\t\t(Пример: 01)')


def draw_board():
    print(f'\n\t\t\t  0   1   2\n\t\t\t-------------')
    for i, row in enumerate(board):
        row_str = f'\t\t {i}  | {" | ".join(row)} |'
        print(row_str)
        print(f'\t\t\t-------------')


def take_inpud(player_token):
    while True:
        value = input('\nКуда поставить: ' + player_token + ' ? ')

        if str(value) not in '001021011220212' and len(value) >= 3:
            print('Неверный ввод. Повторите.')
            continue
        value1 = [int(i) for i in value]

        if board[value1[0]][value1[1]] != ' ':
            print('Эта клетка уже занята.')
            continue
        board[value1[0]][value1[1]] = player_token
        break

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(board[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            return symbols[0]
        if symbols == ["0", "0", "0"]:
            return symbols[0]
    return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_inpud('X')
        else:
            take_inpud('O')
        if counter > 3:
            winner = check_win()
            if winner:
                draw_board()
                print('\n\t\t*** ВЫИГРАЛ', winner, '! ***')
                break
        counter += 1
        if counter > 8:
            draw_board()
            print('\n\t\t  *** НИЧЬЯ ! ***')
            break


main()

input('\n\nДля выхода нажмите "Enter"')