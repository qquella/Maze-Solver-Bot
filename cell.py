from enum import Flag

from graphics import Window
from point import Line, Point


class Cell:
    """
    holds all the data about an individual cell. It should know which walls it has, where it exists on the canvas in x/y coordinates, and access to the window so that it can draw itself.
    """

    def __init__(self, win=None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            l1 = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(l1)
        else:
            l1 = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(l1, "white")

        if self.has_right_wall:
            l2 = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(l2)
        else:
            l2 = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(l2, "white")

        if self.has_top_wall:
            l3 = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(l3)

        else:
            l3 = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(l3, "white")

        if self.has_bottom_wall:
            l4 = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(l4)

        else:
            l4 = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(l4, "white")

    def draw_move(self, to_cell, undo=False):
        half_len1 = abs(self._x1 - self._x2) // 2
        center_x1 = half_len1 + self._x1
        center_y1 = half_len1 + self._y1

        half_len2 = abs(to_cell._x1 - to_cell._x2) // 2
        center_x2 = half_len2 + to_cell._x1
        center_y2 = half_len2 + to_cell._y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(center_x1, center_y1), Point(center_x2, center_y2))
        self._win.draw_line(line, fill_color)
