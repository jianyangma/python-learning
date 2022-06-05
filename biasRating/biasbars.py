"""
File: biasbars.py
---------------------
Add your comments here
"""

import tkinter
import biasbarsdata
import biasbarsgui as gui


# Provided constants to load and plot the word frequency data
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

FILENAME = "data/full-data.txt"

VERTICAL_MARGIN = 30
LEFT_MARGIN = 60
RIGHT_MARGIN = 30
LABELS = ["Low Reviews", "Medium Reviews", "High Reviews"]
LABEL_OFFSET = 10
BAR_WIDTH = 75
LINE_WIDTH = 2
TEXT_DX = 2
NUM_VERTICAL_DIVISIONS = 7
TICK_WIDTH = 15


def get_centered_x_coordinate(width, idx):
    """
    Given the width of the canvas and the index of the current review
    quality bucket to plot, returns the x coordinate of the centered
    location for the bars and label to be plotted relative to.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current label in the LABELS list
    Returns:
        x_coordinate (float): The centered x coordinate of the horizontal line 
                              associated with the specified label.
    >>> round(get_centered_x_coordinate(1000, 0), 1)
    211.7
    >>> round(get_centered_x_coordinate(1000, 1), 1)
    515.0
    >>> round(get_centered_x_coordinate(1000, 2), 1)
    818.3
    """
    size = (WINDOW_WIDTH - LEFT_MARGIN - RIGHT_MARGIN) / 3
    return (size / 2 + LEFT_MARGIN) + size * idx


def draw_fixed_content(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background border and x-axis labels on it.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing content from the canvas
    width = canvas.winfo_width()    # get the width of the canvas
    height = canvas.winfo_height()  # get the height of the canvas
    canvas.create_rectangle(0 + LEFT_MARGIN, 0 + VERTICAL_MARGIN, WINDOW_WIDTH - RIGHT_MARGIN,
                            WINDOW_HEIGHT - VERTICAL_MARGIN, width=LINE_WIDTH)
    canvas.create_text(get_centered_x_coordinate(WINDOW_WIDTH, 0), WINDOW_HEIGHT - VERTICAL_MARGIN + LABEL_OFFSET,
                       anchor=tkinter.N, text='Low Reviews')
    canvas.create_text(get_centered_x_coordinate(WINDOW_WIDTH, 1), WINDOW_HEIGHT - VERTICAL_MARGIN + LABEL_OFFSET,
                       anchor=tkinter.N, text='Medium Reviews')
    canvas.create_text(get_centered_x_coordinate(WINDOW_WIDTH, 2), WINDOW_HEIGHT - VERTICAL_MARGIN + LABEL_OFFSET,
                       anchor=tkinter.N, text='High Reviews')


def plot_word(canvas, word_data, word):
    """
    Given a dictionary of word frequency data and a single word, plots
    the distribution of the frequency of this word across gender and 
    rating category.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
        word_data (dictionary): Dictionary holding word frequency data
        word (str): The word whose frequency distribution you want to plot
    """

    draw_fixed_content(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    gender_data = word_data[word]
    max_frequency = max(max(gender_data[biasbarsdata.KEY_WOMEN]), max(gender_data[biasbarsdata.KEY_MEN]))

    w_color = 'mistyrose'
    m_color='aquamarine'
    gap_value = max_frequency / NUM_VERTICAL_DIVISIONS
    gap = (WINDOW_HEIGHT - VERTICAL_MARGIN - VERTICAL_MARGIN) / NUM_VERTICAL_DIVISIONS
    for i in range(8):
        canvas.create_line(0 + LEFT_MARGIN - TICK_WIDTH / 2, WINDOW_HEIGHT - VERTICAL_MARGIN - gap * i,
                           0 + LEFT_MARGIN + TICK_WIDTH / 2, WINDOW_HEIGHT - VERTICAL_MARGIN - gap * i,
                           width=LINE_WIDTH)
        canvas.create_text(LEFT_MARGIN - LABEL_OFFSET, WINDOW_HEIGHT - VERTICAL_MARGIN - gap * i,
                           anchor=tkinter.E, text=str(int(gap_value * i)))
    for i in range(3):
        w_low = gender_data[biasbarsdata.KEY_WOMEN][i]
        dist_ratio = w_low / gap_value
        if w_low != 0:
            canvas.create_rectangle(get_centered_x_coordinate(1000, i) - BAR_WIDTH,
                                WINDOW_HEIGHT - VERTICAL_MARGIN - gap * dist_ratio,
                                get_centered_x_coordinate(1000, i), WINDOW_HEIGHT - VERTICAL_MARGIN, fill=w_color)
            canvas.create_text(get_centered_x_coordinate(1000, i) - BAR_WIDTH + TEXT_DX,
                               WINDOW_HEIGHT - VERTICAL_MARGIN - gap * dist_ratio,
                               anchor=tkinter.NW, text='W')
        m_low = gender_data[biasbarsdata.KEY_MEN][i]
        dist_ratio = m_low / gap_value
        if m_low != 0:
            canvas.create_rectangle(get_centered_x_coordinate(1000, i),
                                WINDOW_HEIGHT - VERTICAL_MARGIN - gap * dist_ratio,
                                get_centered_x_coordinate(1000, i) + BAR_WIDTH, WINDOW_HEIGHT - VERTICAL_MARGIN,
                                fill=m_color)
            canvas.create_text(get_centered_x_coordinate(1000, i) + TEXT_DX,
                               WINDOW_HEIGHT - VERTICAL_MARGIN - gap * dist_ratio,
                               anchor=tkinter.NW, text='M')


def convert_counts_to_frequencies(word_data):
    """
    Converts a dictionary
    of word counts into a dictionary of word frequencies by 
    dividing each count for a given gender by the total number 
    of words found in reviews about professors of that gender.
    """ 
    K = 1000000
    total_words_men = sum([sum(counts[biasbarsdata.KEY_MEN]) for word, counts in word_data.items()])
    total_words_women = sum([sum(counts[biasbarsdata.KEY_WOMEN]) for word, counts in word_data.items()])
    for word in word_data:
        gender_data = word_data[word]
        for i in range(3):
            gender_data[biasbarsdata.KEY_MEN][i] *= K / total_words_men
            gender_data[biasbarsdata.KEY_WOMEN][i] *= K / total_words_women


# main() code is provided for you
def main():
    import sys
    args = sys.argv[1:]
    global WINDOW_WIDTH
    global WINDOW_HEIGHT
    if len(args) == 2:
        WINDOW_WIDTH = int(args[0])
        WINDOW_HEIGHT = int(args[1])

    # Load data
    word_data = biasbarsdata.read_file(FILENAME)
    convert_counts_to_frequencies(word_data)

    # Make window
    top = tkinter.Tk()
    top.wm_title('Bias Bars')
    canvas = gui.make_gui(top, WINDOW_WIDTH, WINDOW_HEIGHT, word_data, plot_word, biasbarsdata.search_words)

    # draw_fixed once at startup so we have the borders and labels
    # even before the user types anything.
    draw_fixed_content(canvas)

    # This needs to be called just once
    top.mainloop()


if __name__ == '__main__':
    main()
