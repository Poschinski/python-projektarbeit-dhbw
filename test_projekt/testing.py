import sys
import os

if os.name == "nt":
    import msvcrt
else:
    import tty
    import termios

while True:
    if os.name == "nt":
        #ch = msvcrt.getch().decode('utf-8')
        ch = ord(msvcrt.getch())
        print(ch)
        if ch == "b":
            break
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        print(ch)
        if ch == "b":
            break