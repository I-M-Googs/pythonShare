def print_field(cells_in):
    count = line_count = line_plays = 0
    for i in range(2):
        print(f'---------')
        if i == 1:
            break
        while line_count < 3:
            print(f'| ', end='')
            while line_plays < 3:
                print(f'{cells_in[count]} ', end='')
                count += 1
                line_plays += 1
            print('|')
            line_plays = 0
            line_count += 1


def player(counter):
    if counter % 2 == 0:
        return 'X'
    else:
        return 'O'


def get_move():
    move_list = []
    entry = []
    move = input('Enter the coordinates: ')
    for i in range(len(move)):
        if move[i].isdigit():
            move_list.append(int(move[i]))
    entry.append(tuple(move_list))
    return entry


def results(cells_played):
    plays = [i for i in cells_played if (i == 'O' or i == 'X')]
    played = len(plays)
    row_1 = cells_played[0:3]
    row_2 = cells_played[3:6]
    row_3 = cells_played[6:9]
    column_1 = cells_played[0:9:3]
    column_2 = cells_played[1:9:3]
    column_3 = cells_played[2:9:3]
    diagonal_1 = cells_played[0] + cells_played[4] + cells_played[8]
    diagonal_2 = cells_played[2] + cells_played[4] + cells_played[6]


    possible_winners = [row_1, row_2, row_3, column_1, column_2, column_3, diagonal_1, diagonal_2]
    c = [i == 'XXX' for i in possible_winners]
    d = [i == 'OOO' for i in possible_winners]
    if True in c and True not in d:
        result = '\nX wins'
        return result
    elif True in d and True not in c:
        result = '\nO wins'
        return result
    elif played < 5 or (True not in c or d) and played < 9:
        result = 'no_winner'
        return result
    else:
        result = '\nDraw'
        return result


def list_to_string(list_in):
    new_string = ''
    return(new_string.join(list_in))


def game():    
    full_grid = [(y, x) for x in [3, 2, 1] for y in [1, 2, 3]]
    cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    prior_plays = []
    current_player = 0
    outcome = 'no_winner'
    while outcome == 'no_winner':
        play = get_move()
        if play == [()]:
            print('You should enter numbers!')
        elif not (0 < play[0][0] < 4 and 0 < play[0][1] < 4):
            print('Coordinates should be from 1 to 3!')
        elif play[0] in prior_plays:
            print('This cell is occupied! Choose another one!')
        else:
            prior_plays.append(play[0])
            for i in range(len(full_grid)):
                if play[0] == full_grid[i]:
                    cells.pop(i)
                    cells.insert(i, player(current_player))
                    print_field(cells)
                    current_player += 1
                    status_string = list_to_string(cells)
                    status = results(status_string)
                    if status[3:] == 'wins':
                        outcome = 'winner'
    else:
        print(status)


game()