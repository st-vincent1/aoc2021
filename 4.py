import numpy as np
import sys


class Board:
    def __init__(self, board_data):
        self.rows = board_data
        self.cols = np.transpose(board_data)
        self.dont_check = False
        # self.diags = np.stack((
        #     np.diag(board_data),
        #     np.diag(np.fliplr(board_data)))
        # )
    def check_off_number(self, number):
        check_off = lambda x: np.where(x == number, -1, x)
        self.rows = check_off(self.rows)
        self.cols = check_off(self.cols)
        # self.diags = check_off(self.diags)

    def check_if_done(self):
        means = np.concatenate((
            self.rows.mean(axis=1),
            self.cols.mean(axis=1)
            # self.diags.mean(axis=1)
        ))
        return -1 in means

    def sum_of_unmarked(self):
        self.rows = np.where(self.rows==-1, 0, self.rows)
        return np.sum(self.rows)

""" 4a """

def read_in_data():
    with open('input_file') as f:
        lines = f.read().splitlines()
    numbers = lines[0].split(',')
    numbers = [int(x) for x in numbers]
    with open('input_file_sub') as f:
        lines = f.read().splitlines()
    lines.append('')

    board_data = []
    board = []
    for line in lines:
        row = line.split()
        print(row)
        if row == []:
            board_data.append(np.array(board).astype(int))
            board = []
        else:
            board.append(row)
    return board_data, numbers

def main():
    boards, numbers = read_in_data()
    board_list = []
    for b in boards:
        board_list.append(Board(b))

    """ 4b """
    remaining_boards = len(board_list)

    for k in range(len(numbers)):
        for board in board_list:
            if board.dont_check: continue
            board.check_off_number(numbers[k])
            print(f"Board after checking off {numbers[k]}", board.rows)
            if board.check_if_done():
                """ 4a """
                #print(board.sum_of_unmarked() * numbers[k])
                #sys.exit(1)
                """ 4b """
                if remaining_boards == 1:
                    print(board.sum_of_unmarked() * numbers[k])
                    sys.exit(1)
                else:
                    board.dont_check = True
                    remaining_boards -= 1

if __name__ == '__main__':
    main()

# list of numbers and list of boards (latter as csv)

# function: check if board is done

# function: tick off a number on the board