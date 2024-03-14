board = {1:'-', 2:'-', 3:'-', 4:'-', 5:'-', 6:'-', 7:'-', 8:'-', 9:'-'}

wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (7, 5, 3), (1, 5, 9)]

print('\nДля выбора позиции выберите номер строки по\nвертикали и номер столбца по горизонтали.'
          '\n\t\t\t(Пример: 00)')


def draw_board():
    print('\n\t\t\t    0  1  2'
          '\n\t\t\t 0  {b[1]}  {b[2]}  {b[3]}'
          '\n\t\t\t 1  {b[4]}  {b[5]}  {b[6]}'
          '\n\t\t\t 2  {b[7]}  {b[8]}  {b[9]}'.format(b=board))


def take_inpud(player_token):
    while True:
        num0 = 0
        num1 = 1
        num2 = 2

        value = input('\nКуда поставить: ' + player_token + ' ? ')

        if str(value) not in '001021011220212' and len(value) >= 3:
            print('Ошибочный ввод. Повторите.')
            continue
        if value == str(num0) + str(num0):
            value = 1

        if value == str(num0) + str(num1):
            value = 2

        if value == str(num0) + str(num2):
            value = 3

        if value == str(num1) + str(num0):
            value = 4

        if value == str(num1) + str(num1):
            value = 5

        if value == str(num1) + str(num2):
            value = 6

        if value == str(num2) + str(num0):
            value = 7

        if value == str(num2) + str(num1):
            value = 8

        if value == str(num2) + str(num2):
            value = 9
        if board[value] in 'XO':
            print('Эта клетка уже занята.')
            continue
        board[value] = player_token
        break



def check_win():
    for each in wins_coord:
        if board[each[0]] in 'X' and board[each[1]] in 'X' and board[each[2]] in 'X' or \
                board[each[0]] in 'O' and board[each[1]] in 'O' and board[each[2]] in 'O':
            return board[each[1]]
    else:
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