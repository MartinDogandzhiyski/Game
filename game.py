#place player marker on the spot - check if the columnt is full if so - ask again
#TODO define winning conditions

class InvalidColumnError(Exception):
    pass


class InvalidPlace(Exception):
    pass


def print_matrix(ma):
    for el in ma:
        print(el)


def validate_column_choice(selected_column_num, max_column_index):
    if not (0 <= selected_column_num <= max_column_index):
        raise InvalidColumnError


def player_spot(column_num, matrix, player_num):
    current_row = rows_count - 1
    if matrix[current_row][column_num] == 0:
        matrix[current_row][column_num] = player_num
    else:
        have_space = True
        while not matrix[current_row][column_num] == 0:
            current_row -= 1
            if current_row < 0:
                raise InvalidPlace
        if have_space:
            matrix[current_row][column_num] = player_num
    return column_num, current_row


def is_player_num(ma, row, col, player_num):
    if col < 0 or row < 0:
        return False
    try:
        if ma[row][col] == player_num:
            return True
    except IndexError:
        return False
    return False


def is_horizontal(ma, row, col, player_num, slots_count=4):
    count_right = [is_player_num(ma, row, col + index, player_num) for index in range(slots_count)].count(True)
    count_left = [is_player_num(ma, row, col - index, player_num) for index in range(slots_count)].count(True)
    return (count_left + count_right) >= slots_count


def is_right_diagonal(ma, row, col, player_num, slots_count):
    right_up_count = [is_player_num(ma, row - index, col + index, player_num) for index in range(slots_count)].count(
        True)
    left_down_count = [is_player_num(ma, row + index, col - index, player_num) for index in range(slots_count)].count(
        True)
    return (right_up_count + left_down_count) >= 4


def is_left_diagonal(ma, row, col, player_num, slots_count):
    left_up_count = [is_player_num(ma, row - index, col - index, player_num) for index in range(slots_count)].count(
        True)
    right_down_count = [is_player_num(ma, row + index, col + index, player_num) for index in range(slots_count)].count(
        True)


def is_winner(ma, row, col, player_num, slots_count=4):
    count_right = [is_player_num(ma, row, col + index, player_num) for index in range(slots_count)].count(True)
    count_right = [is_player_num(ma, row, col + index, player_num) for index in range(slots_count)].count(True)
    count_right = [is_player_num(ma, row, col + index, player_num) for index in range(slots_count)].count(True)
    is_up = all([is_player_num(ma, row - index, col, player_num) for index in range(slots_count)])
    is_down = all([is_player_num(ma, row + index, col, player_num) for index in range(slots_count)])


    if any(
            [
                is_down,
                is_horizontal(ma, row, col, player_num, slots_count),
                is_right_diagonal(ma, row, col, player_num, slots_count),
                is_left_diagonal(ma, row, col, player_num, slots_count),
                is_up
            ]

    ):
        return True

    return False


rows_count = 6
cols_count = 7

matrix = [[0 for _ in range(cols_count)] for x in range(rows_count)]
#create matrix
print_matrix(matrix)
#print matrix
player_num = 1
while True:
    player_num = 2 if player_num % 2 == 0 else 1
    try:
        column_num = int(input(f"Player {player_num}, please choose a column: ")) - 1
        validate_column_choice(column_num, cols_count - 1)
        col, row = player_spot(column_num, matrix, player_num)
        if is_winner(matrix, row, col, player_num):
            print_matrix(matrix)
            print(f"The winner is player {player_num}")
            break
        print_matrix(matrix)
        # read column choice from input
        # verify player choice of number of the column - if not ask again
    except InvalidColumnError:
        print(f"This column is not valid. Please select a number between 1 and {cols_count}")
        continue
    except ValueError:
        print("Please select a valid digit")
        continue
    except InvalidPlace:
        print("No more space on this column, select new one")
        continue
    player_num += 1


