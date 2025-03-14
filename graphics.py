from tkinter import BOTH, Canvas, Tk


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed")

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def close(self):
        self.__running = False
