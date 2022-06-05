"""
File: pyramid.py
----------------
ADD YOUR DESCRIPTION HERE
"""

import tkinter

CANVAS_WIDTH = 600  # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300  # Height of drawing canvas in pixels

BRICK_WIDTH = 30  # The width of each brick in pixels
BRICK_HEIGHT = 12  # The height of each brick in pixels
BRICKS_IN_BASE = 2  # The number of bricks in the base


def draw_pyramid(canvas):
    expected = 0
    build = []
    current = 0
    row = 1
    even = BRICKS_IN_BASE % 2 == 0
    for i in range(BRICKS_IN_BASE, 0, -1):
        expected += i
        build.append(i)
    for i in range(len(build)):
        if even:
            count = build_row_even(canvas, row, build[i])
            current += count
            row += 1
            even = False
        else:
            count = build_row_odd(canvas, row, build[i])
            current += count
            row += 1
            even = True


def build_row_even(canvas, row, build):
    count = 0

    for i in range(build // 2):
        canvas.create_rectangle(CANVAS_WIDTH // 2 - BRICK_WIDTH * (i + 1), CANVAS_HEIGHT - BRICK_HEIGHT * row,
                                CANVAS_WIDTH // 2 - BRICK_WIDTH * i, CANVAS_HEIGHT - BRICK_HEIGHT * (row - 1))
        canvas.create_rectangle(CANVAS_WIDTH // 2 + BRICK_WIDTH * (i + 1), CANVAS_HEIGHT - BRICK_HEIGHT * row,
                                CANVAS_WIDTH // 2 + BRICK_WIDTH * i, CANVAS_HEIGHT - BRICK_HEIGHT * (row - 1))
        count += 2
    return count


def build_row_odd(canvas, row, build):
    count = 0
    canvas.create_rectangle(CANVAS_WIDTH // 2 - BRICK_WIDTH // 2, CANVAS_HEIGHT - BRICK_HEIGHT * row,
                            CANVAS_WIDTH // 2 + BRICK_WIDTH // 2, CANVAS_HEIGHT - BRICK_HEIGHT * (row - 1))
    for i in range((build - 1) // 2):
        canvas.create_rectangle(CANVAS_WIDTH // 2 - BRICK_WIDTH // 2 - BRICK_WIDTH * (i + 1),
                                CANVAS_HEIGHT - BRICK_HEIGHT * row,
                                CANVAS_WIDTH // 2 - BRICK_WIDTH // 2 - BRICK_WIDTH * i, CANVAS_HEIGHT - BRICK_HEIGHT * (row - 1))
        canvas.create_rectangle(CANVAS_WIDTH // 2 + BRICK_WIDTH // 2 + BRICK_WIDTH*(i+1),
                                CANVAS_HEIGHT - BRICK_HEIGHT * row,
                                CANVAS_WIDTH // 2 + BRICK_WIDTH // 2 + BRICK_WIDTH * i, CANVAS_HEIGHT - BRICK_HEIGHT * (row - 1))
        count += 2
    return count


# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height):
    """
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('pyramid')
    canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    # Draw blue boundary line at bottom of canvas
    canvas.create_line(0, height, width, height, width=1, fill='blue')

    return canvas


def main():
    """
    This program, when completed, displays a pyramid graphically.
    """
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_pyramid(canvas)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
