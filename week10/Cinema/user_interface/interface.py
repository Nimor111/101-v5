from user_interface.main_menu import *
from termcolor import cprint


def interface():
    """
    Main interface for the console app
    """
    cprint('Welcome to the best cinema in the world!', 'green')
    commands = {'1': show_movies, '2': show_movie_projections,
                '3': make_reservation, '4': cancel_reservation,
                '5': exit, '6': da_help}

    while True:
        cprint("""
              1 - show movies
              2 - show movie projections
              3 - make reservation
              4 - cancel reservation
              5 - exit
              6 - help
              """, 'green')
        cprint("Enter a command>", 'cyan')
        command = input()
        if command == '2':
            cprint('Enter movie id to see projections> ', 'cyan')
            movie = input()
            cprint("""Enter date if you wish, if not press enter,
                         date must be in format yyyy-mm-dd, or the universe
                         will explode.""", 'cyan')
            date = input()
            if date:
                show_movie_projections(movie, date)
            else:
                show_movie_projections(movie)
        elif command == '4':
            cprint('Enter username> ', 'cyan')
            user = input()
            cancel_reservation(user)
        elif command == '3':
            cprint('Enter username> ', 'cyan')
            user = input()
            cprint('Enter password> ', 'cyan')
            password = input()
            make_reservation(user, password)
        else:
            commands[command]()


def main():
    interface()


if __name__ == '__main__':
    main()
