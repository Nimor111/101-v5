from user_interface.main_menu import *


def interface():
    """
    Main interface for the console app
    """
    print("Welcome to the best cinema in the world!")
    commands = {'1': show_movies, '2': show_movie_projections,
                '3': make_reservation, '4': cancel_reservation,
                '5': exit, '6': da_help}

    while True:
        print("""
              1 - show movies
              2 - show movie projections
              3 - make reservation
              4 - cancel reservation
              5 - exit
              6 - help
              """)
        command = input("Enter a command>")
        if command == '2':
            movie = input("Enter movie id to see projections> ")
            date = input("""Enter date if you wish, if not press enter,
                         date must be in format yyyy-mm-dd, or the universe
                         will explode.""")
            if date:
                show_movie_projections(movie, date)
            else:
                show_movie_projections(movie)
        elif command == '4':
            user = input("Enter username> ")
            cancel_reservation(user)
        elif command == '3':
            user = input("Enter username> ")
            password = input("Enter password> ")
            make_reservation(user, password)
        else:
            commands[command]()


def main():
    interface()


if __name__ == '__main__':
    main()
