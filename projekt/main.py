import os

from game import *

if os.name == "nt":
    clearCommand = "cls"
else:
    clearCommand = "clear"

def main(clearCommand):
    """
    Handle menu options
    """
    os.system(clearCommand)

    while True:
        os.system(clearCommand)
        option = input('''
                             ______________________________________________
                          .-'                     _                        '.
                        .'                       |-'                        |
                      .'                         |                          |
                   _.'               p         _\_/_         p              |
                _.'                  |       .'  |  '.       |              |
           __..'                     |      /    |    \      |              |
     ___..'                         .T\    ======+======    /T.             |
  ;;;\::::                        .' | \  /      |      \  / | '.           |
  ;;;|::::                      .'   |  \/       |       \/  |   '.         |
  ;;;/::::                    .'     |   \       |        \  |     '.       |
        ''.__               .'       |    \      |         \ |       '.     |
             ''._          <_________|_____>_____|__________>|_________>    |
                 '._     (___________|___________|___________|___________)  |
                    '.    \;;;;;;;;;;o;;;;;o;;;;;o;;;;;o;;;;;o;;;;;o;;;;/   |
                      '.~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~   |
                        '. ~ ~ ~ ~ ~ ~ ~ ~ ~Battleship ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |
                          '-.______________________________________________.'


Choose option:
(1) Start single player
(2) Start multi player
(3) exit
''')
        if option == '1':
            os.system(clearCommand)

            player_name = input('Enter player name: ')
            difficulty_level = None
            while True:
                try:
                    os.system(clearCommand)
                    difficulty_level = int(input('Enter difficulty of computer player(0:easy, 1:medium, 2:hard): '))
                    if difficulty_level in [0, 1, 2]: break
                except:
                    continue
            os.system(clearCommand)
            singleplayer_game = SingleGame(player_name, difficulty_level, clearCommand)
            singleplayer_game.start_game()

        elif option == '2':
            os.system(clearCommand)

            player_name1 = input('Enter name of 1st player: ')
            player_name2 = input('Enter name of 2nd player: ')

            multiplayer_game = MultiPlayerGame(player_name1, player_name2, clearCommand)
            multiplayer_game.start_game()

        elif option == '3':
            os.system(clearCommand)
            exit("Thanks for playing.")


if __name__ == "__main__":
    main(clearCommand)
