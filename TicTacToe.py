from math import sqrt
from random import choice,randint

class TicTacToe:
    def __init__(self):
        self.board = []
        self.mode = self.getBoardSize()
        self.players = [' x ',' o ']

        self.current_player = choice(self.players)

    def start(self):
        print(f'First move - {self.current_player}')

        self.createBoard()
        while True:
            self.drawBoard()
            self.makeMove()
            if self.isWin(self.current_player):
                print(f"Congratulations {self.current_player} - winner")
                self.drawBoard()
                exit(0)
            if self.isBoardFilled():
                print("Draw")
                self.drawBoard()
                exit(0)
            self.changeCurrentPlayer()

    def createBoard(self):
        for i in range(self.mode):
            row = []
            for j in range(self.mode):
                row.append(' - ')
            self.board.append(row)
                
    
    def drawBoard(self):
        for i in range(self.mode):
            for j in range(self.mode):
                print(self.board[i][j], end='')
            print('')

    def makeMove(self):
        col = input('Enter column number: ')
        row = input('Enter row number: ')
        if self.checkMoveValues(col,row):
            self.board[int(row)-1][int(col)-1] = self.current_player

    def getBoardSize(self):
        while True:
            mode = input("Enter board size (3,4,5...) it means 3x3,5x5...: ")
            if mode.isnumeric():
                return int(mode)
                

    def changeCurrentPlayer(self):
        if self.current_player == ' x ':
            self.current_player = ' o '
        else:
            self.current_player = ' x '    
        
    def checkMoveValues(self, col, row):
        if col.isnumeric() and row.isnumeric():
            if int(col) <= self.mode and int(row) <= self.mode:
                return True
    
    def isWin(self, player):
        win = None
        size = self.mode

        # Checking colums
        for i in range(size):
            win = True
            for j in range(size):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # Checking rows
        for i in range(size):
            win = True
            for j in range(size):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # Checking left diagonal
        win = True
        for i in range(size):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        # Checking right diagonal
        win = True
        for i in range(size):
            if self.board[size-1-i][i] != player:
                win = False
                break
        if win:
            return win

    def isBoardFilled(self):
        for i in range(self.mode):
            for j in range(self.mode):
                if self.board[i][j] == ' - ':
                    return False
        return True