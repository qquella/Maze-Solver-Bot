from graphics import Window
from point import Line, Point


class Cell:
    """
    holds all the data about an individual cell. It should know which walls it has, where it exists on the canvas in x/y coordinates, and access to the window so that it can draw itself.
    """

    def __init__(self, win: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            l1 = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(l1)
        if self.has_right_wall:
            l2 = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(l2)
        if self.has_top_wall:
            l3 = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(l3)
        if self.has_bottom_wall:
            l4 = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(l4)
