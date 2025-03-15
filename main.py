from graphics import Window
from point import Line, Point


def main():
    win = Window(800, 600)

    # draw some points and lines
    p1 = Point(50, 50)
    p2 = Point(400, 400)
    l1 = Line(p1, p2)

    win.draw_line(l1, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()
