cells = ' ' * 9
rows = [cells[:3], cells[3:6], cells[6:]]


def print_grid():
    print('---------')
    for row in rows:
        print(f'| {row[0]} {row[1]} {row[2]} |')
    print('---------')


def make_move(symbol='X'):
    while True:
        try:
            user_input = [int(number) - 1 for number in input('Enter the coordinates: ').split()]
        except ValueError:
            print('You should enter numbers!')
            continue
        else:
            if not (0 <= user_input[0] <= 2 and 0 <= user_input[1] <= 2):
                print('Coordinates should be from 1 to 3!')
                continue
            elif rows[user_input[0]][user_input[1]] != ' ':
                print('This cell is occupied! Choose another one!')
                continue
            else:
                updated_row = [symbol if i == user_input[1] else rows[user_input[0]][i] for i in range(3)]
                rows[user_input[0]] = ''.join(updated_row)
                print_grid()
                check_winner(symbol)


def check_winner(symbol):
    columns = [rows[0][0] + rows[1][0] + rows[2][0],
               rows[0][1] + rows[1][1] + rows[2][1],
               rows[0][2] + rows[1][2] + rows[2][2]]
    diagonals = [rows[0][0] + rows[1][1] + rows[2][2],
                 rows[0][2] + rows[1][1] + rows[2][0]]
    combinations = rows + columns + diagonals
    if 'XXX' in combinations:
        print('X wins')
        quit()
    elif 'OOO' in combinations:
        print('O wins')
        quit()
    elif ' ' not in ''.join(rows):
        print('Draw')
        quit()
    else:
        if symbol == 'X':
            make_move('O')
        elif symbol == 'O':
            make_move('X')


if __name__ == '__main__':
    print_grid()
    make_move()
