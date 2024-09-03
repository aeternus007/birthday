from os import path
from time import sleep

try:
    import curses
    from curses import wrapper
    
except:
    import windows_curses as curses
    from windows_curses import wrapper


class Message_points:
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def update(self, screen, size):
        if self.char == "(":
            self.char = ")"
        elif self.char == ")":
            self.char = "("
        elif self.char == "∽":
            self.char = "~"
        elif self.char == "~":
            self.char = "∽"
        else:
            pass


        screen.addch(self.y, self.x, self.char, self.color)


def main(screen, message_path):
    # Color constants
    BLCK = curses.COLOR_BLACK
    BLINK = curses.A_BLINK
    curses.init_pair(1, curses.COLOR_YELLOW, BLCK)
    YELLOW = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_WHITE, BLCK)
    DEFAULT = curses.color_pair(2)

    screen_size = screen.getmaxyx()
    message_points = []
    message_size = [0, 0]

    with open(message_path, 'r') as message:
        for y, line in enumerate((message := message.readlines())):
            for x, char in enumerate(line):
                if char == "*":
                    message_points.append(Message_points(x, y, char, YELLOW | BLINK))
                elif char in "()":
                    message_points.append(Message_points(x, y, char, YELLOW))
                elif char != " " and char != "\n":
                    message_points.append(Message_points(x, y, char, DEFAULT))
                else:
                    pass

    while True:
        screen.clear()
        for point in message_points:
            point.update(screen, screen_size)

        sleep(0.4)
        screen.refresh()


message = path.join(path.dirname(__file__), 'message.txt') # make a universal path

wrapper(main, message)