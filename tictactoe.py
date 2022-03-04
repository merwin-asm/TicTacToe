import random

class Tictoe:
    def __init__(self,board=(3,3),player="x",opponent="o"):
        self.game_board = self.make_board(board)
        self.player = player
        self.opponent = opponent
    def make_board(self,dim):
        return [["_" for x in range(dim[1])] for y in range(dim[0])]
    def make_move(self,y_x,player=True):
        if player:
            self.game_board[y_x[0]][y_x[1]] = self.player
        else:
            self.game_board[y_x[0]][y_x[1]] = self.opponent

    def scan_for_cross(self):
        l = self.game_board
        y = 0
        for e in l:
            if e[0] == e[1] == e[2]:
                return True, ("x", y), e[0]
            y += 1
        if l[0][0] == l[1][0] == l[2][0]:
            return True, ("y", 0), l[0][0]
        if l[0][1] == l[1][1] == l[2][1]:
            return True, ("y", 1), l[0][1]
        if l[0][2] == l[1][2] == l[2][2]:
            return True, ("y", 2), l[0][2]
        if l[0][0] == l[1][1] == l[2][2]:
            return True, ("Cross", "a"), l[0][0]
        if l[0][2] == l[1][1] == l[2][0]:
            return True, ("Cross", "b"), l[0][2]
        return False
    def show_current(self,display=True):
        out = """"""
        for e in self.game_board:
            out+=" | "
            for i in e:
                out+=i
                out+=" | "
            out+="\n"
        if display:
            print(out)
        return out
    def cross_out(self,info):
        if info[0] == "y":
            self.game_board[0][info[1]] = "-"
            self.game_board[1][info[1]] = "-"
            self.game_board[2][info[1]] = "-"
        elif info[0] == "x":
            self.game_board[info[1]] = ["-","-","-"]
        elif info[0] == "Cross":
            if info[1] == "a":
                self.game_board[0][0] = "-"
                self.game_board[1][1] = "-"
                self.game_board[2][2] = "-"
            else:
                self.game_board[0][2] = "-"
                self.game_board[1][1] = "-"
                self.game_board[2][0] = "-"
    def get_free_pos(self):
        available = []
        x = 0
        y = 0
        for e in self.game_board:
            for i in e:
                if i == "_":
                    available.append([y,x])
                x+=1
            y+=1
            x = 0
        return available
    def auto_move(self):
        self.make_move(random.choice(self.get_free_pos()),player=False)

if __name__ == '__main__':
    while True :
        tik_tak_toe = Tictoe()
        print("TicTacToe!")
        print("")
        print("Press 's' to stop the game.")
        print("///////////")
        print("")
        inp = ""
        while inp != "s":
            tik_tak_toe.show_current()
            inp = input("U r turn Type in Coordinates(y,x) : ")
            inp = inp.split(",")
            inp = (int(inp[0]),int(inp[1]))
            tik_tak_toe.make_move(inp)
            scan_res = tik_tak_toe.scan_for_cross()
            if scan_res != False:
                if scan_res[2] != "_":
                    info = scan_res[1]
                    player = scan_res[2]
                    tik_tak_toe.cross_out(info)
                    tik_tak_toe.show_current()
                    print(f"{player} Won the match!")
                    break
            tik_tak_toe.auto_move()
            scan_res = tik_tak_toe.scan_for_cross()
            if scan_res != False:
                if scan_res[2] != "_":
                    info = scan_res[1]
                    player = scan_res[2]
                    tik_tak_toe.cross_out(info)
                    tik_tak_toe.show_current()
                    print(f"{player} Won the match!")
                    break
        input("Press enter to play again !")
