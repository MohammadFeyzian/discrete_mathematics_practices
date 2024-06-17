# ToDo: complete this logic
size = 5
target = 16
board = [[0 for _ in range(size)] for _ in range(size)]


def bt(board, row, start):
    if len(board) == size:
        if is_the_solution(board):
            print(board)
            exit()

    if len(row) == size:
        board.append(list(row))
        return

    for i in range(start, size):
        print(row)
        print(board)
        if can_be_added(board, i, len(board), 1):
            row.append(1)
            bt(board, row, start + 1)
            row.pop()
        elif can_be_added(board, i, len(board), 2):
            row.append(2)
            bt(board, row, start + 1)
            row.pop()
        else:
            row.append(0)
            bt(board, row, start + 1)
            row.pop()
        bt(board, row, 0)


def can_be_added(board, i, j, value):
    print("---------------")
    print(f"i = {i} , j = {j} , value = {value}")
    print("---------------")
    if value == 1:
        if (i > 0 and j > 0 and board[i - 1][j] == 2) or (
                j > 0 and board[i][j - 1] == 2) \
                or (j > 0 and i < size - 2
                    and (board[i + 1][j - 1] == 1)):
            return False

    if value == 2:
        if (i > 0 and board[i - 1][j] == 1) or (
                j > 0 and board[i][j - 1] == 1) or (i > 0 and j > 0 and board[i - 1][j - 1] == 2):
            return False

    return True


def is_the_solution(colum):
    counter = 0
    for row in colum:
        for cell in row:
            if cell == 1 or cell == 2:
                counter += 1

    return counter == target


def print_board():
    for row in board:
        print(row)


bt(board, [], 0)
