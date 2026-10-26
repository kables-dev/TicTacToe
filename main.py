import tkinter as tk

class window:
    def __init__(self):
        self.label = "Tic Tac Toe!"
        self.size = "600x600"
        self.background_color = "white"

        self.root = tk.Tk()

    def open(self):
        self.root.title(self.label)
        self.root.geometry(self.size)  # Width x Height

        self.root.configure(background=self.background_color)

        # 4. Start the application event loop
        self.root.mainloop()


class board:
    def __init__(self, parent, game_manager, player_turn):
        self.parent = parent 
        self.game_manager = game_manager
        self.rows , self.cols = 3,3
        self.player_turn = player_turn


        self.player = "x"
 
    def on_button_click(self, event):
        clicked_widget = event.widget
        
        info = clicked_widget.grid_info()

        row = info.get("row")
        col = info.get("column")

        #self.game_manager.board_pos[row].insert(col, self.player_turn.decide())
        current_player = self.player_turn.decide()
        self.game_manager.board_pos[row][col] = current_player 
        
        print(f"{col}, {row}")


        self.game_manager.check_winner()

    def draw_grid(self):
        for i in range(self.rows):
            self.parent.rowconfigure(i, weight = 1)
        for j in range(self.cols):
            self.parent.columnconfigure(j, weight = 1)
        
        for r in range(self.rows):
                for c in range(self.cols):
                    btn = tk.Button(self.parent, text = f"{r},{c}",bg = "yellow")
                    btn.grid(row=r, column=c, sticky="nsew")

                    btn.bind("<Button-1>", self.on_button_click)

class player_turn:
    def __init__(self):
        self.player_current = "x"
        self.turn_count = 1
        

    def decide(self):
            if self.turn_count % 2 ==0:
                self.player_current = "o"
            else:
                self.player_current = "x"

            self.turn_count += 1
            
            return self.player_current



class game_manager():
    def __init__(self):

        self.board_pos = [[0] * 3 for _ in range(3)] 
        self.player_char_x = "x"
        self.player_char_o = "o"

    def check_winner(self):
        # Check rows
        for row in self.board_pos:
            if all(pos == self.player_char_x for pos in row):
                print(f"{self.player_char_x} has won the game")
                return

            elif all(pos == self.player_char_o for pos in row):
                print(f"{self.player_char_o} has won the game")
                return

        # Check columns
        for col in range(3):
            column = [self.board_pos[row][col] for row in range(3)]

            if all(pos == self.player_char_x for pos in column):
                print(f"{self.player_char_x} has won the game")
                return

            elif all(pos == self.player_char_o for pos in column):
                print(f"{self.player_char_o} has won the game")
                return

        # Check diagonals
        diagonals = [
            [self.board_pos[0][0], self.board_pos[1][1], self.board_pos[2][2]],
            [self.board_pos[0][2], self.board_pos[1][1], self.board_pos[2][0]]
        ]

        for diagonal in diagonals:
            if all(pos == self.player_char_x for pos in diagonal):
                print(f"{self.player_char_x} has won the game")
                return

            elif all(pos == self.player_char_o for pos in diagonal):
                print(f"{self.player_char_o} has won the game")
                return       
            

            """
                x o x 
                o x o 
                o o o 
            """

def main():
    Window = window()
    Game_manager = game_manager()
    Player_turn = player_turn() 
    Board =board(Window.root, Game_manager, Player_turn)
    Board.draw_grid()
    Window.open()
    print(Game_manager.board_pos)

if __name__ == "__main__":
    main()