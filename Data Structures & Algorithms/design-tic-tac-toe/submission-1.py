class TicTacToe:

    def __init__(self, n: int):
        self.winner = 0
        self.board = []
        for i in range(n):
            self.board.append([])
            for j in range(n):
                self.board[i].append(0)

    def move(self, row: int, col: int, player: int) -> int:
        n = len(self.board)
        if self.winner != 0 or self.board[row][col] != 0:
            return self.winner
        
        self.board[row][col] = player
        complete = 4
        for i in range(n):
            if self.board[i][col] != player:
                complete -= 1
                break
        
        for i in range(n):
            if self.board[row][i] != player:
                complete -= 1
                break
        
        x, y = 0, 0
        while x < n and y < n:
            if self.board[x][y] != player:
                complete -= 1
                break
            x += 1
            y += 1

        x, y = n-1, 0
        while x >= 0 and y < n:
            if self.board[x][y] != player:
                complete -= 1
                break
            x -= 1
            y += 1
        
        if complete > 0:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
