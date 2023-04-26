import curses

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    field = [[0 for x in range(10)] for y in range(10)]
    x, y = 0, 0
    orientation = 'vertical'

    def get_selection():
        if orientation == 'vertical':
            return [(y - i, x) for i in range(3) if y - i >= 0]
        else:
            return [(y, x + i) for i in range(3) if x + i < 10]

    while True:
        stdscr.clear()
        selection = get_selection()
        for row in range(len(field)):
            for col in range(len(field[row])):
                if (row, col) in selection:
                    stdscr.addstr('X')
                else:
                    stdscr.addstr(str(field[row][col]))
            stdscr.addstr('\n')

        key = stdscr.getch()

        if key == curses.KEY_UP and y > 0:
            y -= 1
        elif key == curses.KEY_DOWN and y < 9:
            y += 1
        elif key == curses.KEY_LEFT and x > 0:
            x -= 1
        elif key == curses.KEY_RIGHT and x < 9:
            x += 1
        elif key == ord('\n'):
            for row, col in selection:
                field[row][col] = (field[row][col] + 1) % 2
        elif key == ord('r'):
            orientation = 'horizontal' if orientation == 'vertical' else 'vertical'

curses.wrapper(main)
