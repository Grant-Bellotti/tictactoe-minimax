class Board:
    def __init__(self):
        # board is a list of cells that are represented 
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented 
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        # the winner's sign O or X
        self.winner = ""
    def get_size(self): 
        return self.size

    def get_winner(self):   
        return self.winner

    def get_board(self,index):     
        return self.board[int(index)]
    
    #set the board with no checks (for MiniMax ONLY)
    def setNoCheck(self, index, sign):
        self.board[index] = sign
        
    def set(self, cell, sign):
        #checks if input is valid
        index = 0
        try:
            int(cell[1])
        except:
            return False

        if (int(cell[1]) > 3 or int(cell[1]) < 1) or len(cell) > 2:
            return False
            
        #convert into list index
        if "A" in cell:
            index = (1 + ((int(cell[1])-1)*3))-1
        elif "B" in cell:
            index = (2 + ((int(cell[1])-1)*3))-1
        elif "C" in cell:
            index = (3 + ((int(cell[1])-1)*3))-1
        else:
            return False
        if self.isempty(index):
            self.board[index] = sign
            return True
        return False

    def isempty(self, cell):
        #checks if space is empty
        if self.board[cell] == " ":
            return True
        return False

    def isdone(self):
        # check all game terminating conditions
        row1 = self.board[0:3] #row1
        row2 = self.board[3:6] #row2
        row3 = self.board[6:9] #row3
        col1 = list(row1[0]) + list(row2[0]) + list(row3[0]) #col1
        col2 = list(row1[1]) + list(row2[1]) + list(row3[1]) #col2
        col3 = list(row1[2]) + list(row2[2]) + list(row3[2]) #col3
        diag1 = list(row1[0]) + list(row2[1]) + list(row3[2]) #diag1
        diag2 = list(row1[2]) + list(row2[1]) + list(row3[0]) #diag2

        if (row1 == ['X','X','X']):
            self.winner = "X"
            return True
        elif (row1 == ['O','O','O']):
            self.winner = "O"
            return True

        if (row2 == ['X','X','X']):
            self.winner = "X"
            return True
        elif (row2 == ['O','O','O']):
            self.winner = "O"
            return True
        
        if (row3 == ['X','X','X']):
            self.winner = "X"
            return True
        elif (row3 == ['O','O','O']):
            self.winner = "O"
            return True

        if (col1 == ['X','X','X']):
            self.winner = "X"
            return True
        elif (col1 == ['O','O','O']):
            self.winner = "O"
            return True

        if (col2 == ['X','X','X']):
            self.winner = "X"
            return True
        elif (col2 == ['O','O','O']):
            self.winner = "O"
            return True

        if (col3 == ['X','X','X']):
            self.winner = "X"
            return True
        elif (col3 == ['O','O','O']):
            self.winner = "O"
            return True

        if (diag1 == ['X','X','X']):
            self.winner = "X"
            return True
        elif (diag1 == ['O','O','O']):
            self.winner = "O"
            return True

        if (diag2 == ['X','X','X']):
            self.winner = "X"
            return True
        elif (diag2 == ['O','O','O']):
            self.winner = "O"
            return True
        
        if " " in self.board:
            self.winner = ''
            return False
            
        self.winner = ''
        return True

    def show(self):
        # draw the board
        board = '\n   A   B   C \n'+' +---+---+---+'
        for i in range(self.size):
            i += 1
            board += '\n'+str(i) + '|'
            for j in range((i-1)*3, i*3):
                board += f' {self.board[j]} |'
            board += '\n +---+---+---+'
        #board += '\n'
        print(board)
            