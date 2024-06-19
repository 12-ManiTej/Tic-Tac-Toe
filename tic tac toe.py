#BUT NOT APPLICABLE FOR DRAW MATCH
class Game:
    def __init__(self):
        self.board=[]
    def create_board(self):
        for i in range(3):
            row=[]
            for j in range(3):
                row.append('-')
            self.board.append(row)
        print(self.board)
    def display_board(self):
        for row in self.board:
            for item in row:
                print(item,end=" ")
            print()
    def board_full(self):
        for row in self.board:
            for item in row:
                if item!='-':
                    return True
        return False
    def swap_player(self,player):
        if player=='O':
            return 'X'
        elif player=='X':
            return 'O'
    def set_player(self,row,column,player):
        self.board[row][column]=player
    def is_playerwin(self,player):
        win=None
        for i in range(3):
            win=True
            for j in range(3):
                if self.board[i][j]!=player:
                    win=False
                    break
            if win:
                return win
            else:
                break
        for i in range(3):
            win=True
            for j in range(3):
                if self.board[j][i]!=player:
                    win=False
            if win:
                return win
            else:
                break
        win=True
        for i in range(3):
            if self.board[i][i]!=player:
                win=False
                break
        if win:
            return win
        for i in range(3):
            win=True
            if self.board[i][2-i]!=player:
                win=False
                break
        if win:
            return win
    def start(self):
        self.create_board()
        import random
        lst=['O','X']
        player=random.choice(lst)
        while(1):
            print(player,'turn')
            row,column=list(map(int,input("enter the row and column:").split()))
            self.set_player(row,column,player)
            self.display_board()
            if self.is_playerwin(player):
                print(player,'won the match')
                break
            '''if self.board_full:
                print("MATCH DRAW")
                break'''
            player=self.swap_player(player)

            
o1=Game()
o1.start()
o1.board_full()
