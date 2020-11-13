def print_cells_in(a):
    cell_count = 0
    field_width = 9
    width_count = 0
    height_count = 0
    while height_count < 5:
        if height_count == 0:
            while width_count < field_width:
                print('-', end='')
                width_count += 1
            else:
                width_count = 0
                height_count += 1
        elif height_count == 1:
            print('\n|', end=' ')
            while cell_count < 3:
                print(a[cell_count], end=' ')
                cell_count += 1
            else:
                print('|', end='')
                height_count += 1
        elif height_count == 2:
            print('\n|', end=' ')
            while cell_count < 6:
                print(a[cell_count], end=' ')
                cell_count += 1
            else:
                print('|', end='')
                height_count += 1
        elif height_count == 3:
            print('\n|', end=' ')
            while cell_count < 9:
                print(a[cell_count], end=' ')
                cell_count += 1
            else:
                height_count += 1
                print('|', end='')
        elif height_count == 4:
            print('\n', end='')
            while width_count < field_width:
                print('-', end='')
                width_count += 1
            else:
                break


def results(a):
    plays = [i for i in a if (i == 'O' or i == 'X')]
    played = len(plays)
    row_1 = a[0:3]
    row_2 = a[3:6]
    row_3 = a[6:9]
    column_1 = a[0:9:3]
    column_2 = a[1:9:3]
    column_3 = a[2:9:3]
    diagonal_1 = a[0] + a[4] + a[8]
    diagonal_2 = a[2] + a[4] + a[6]

    possible_winners = [row_1, row_2, row_3, column_1, column_2, column_3, diagonal_1, diagonal_2]
    c = [i == 'XXX' for i in possible_winners]
    d = [i == 'OOO' for i in possible_winners]
    if (True in c and True in d) or a[0] != 'X':
        print('\nImpossible')
    elif True in c and True not in d:
        print('\nX wins')
    elif True in d and True not in c:
        print('\nO wins')
    elif played < 5 or (True not in c or d) and played < 9:
        print('\nGame not finished')
    else:
        print('\nDraw')


def game():
    cells = input('Enter cells: ')
    print_cells_in(cells)
    results(cells)


game()

