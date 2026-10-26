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
    def __init__(self, parent, game_manager):
        self.parent = parent 
        self.game_manager = game_manager
        self.rows , self.cols = 3,3


        self.player = "x"
 
    def on_button_click(self, event):
        clicked_widget = event.widget
        
        info = clicked_widget.grid_info()

        row = info.get("row")
        col = info.get("column")

        self.game_manager.board_pos[row].insert(col, "x" )
        print(f"{col}, {row}")

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


class game_manager():
    def __init__(self):

        self.board_pos = [[0] * 3 for _ in range(3)] 
        """
            x o x 
            o x o 
            o o o 
        """

def main():
    Window = window()
    Game_manager = game_manager()
    Board =board(Window.root, Game_manager)
    Board.draw_grid()
    Window.open()
    print(Game_manager.board_pos)

if __name__ == "__main__":
    main()