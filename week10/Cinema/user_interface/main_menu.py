from decorators.user_exists import user_exists
from database.modify_database import *
from settings.reservations import reservations
from settings.general_settings import PROJECTIONS
from decorators.log_info import log_info
import sys
from termcolor import cprint


@log_info
def finalize(user_id, projection_id, seats):
    """
    Method called to enter reservations into the database
    """
    for seat in seats:
        insert_reservation(user_id, projection_id, seat[0], seat[1])


@user_exists
def make_reservation(user, password=None):
    """
    The main menu of the program a.k.a the main functions of the CLI
    """
    cprint("Hello, {}".format(user), 'yellow')
    tickets = int(input("Step 1 (User): Choose number of tickets>"))
    show_movies()
    movie = input("Step 2 (Movie) : Choose a movie> ")
    show_movie_projections(movie)
    projection = int(input("Step 3 (Projection): Choose a projection>"))
    proj = Projection(projection)
    proj.hall = PROJECTIONS[projection - 1].hall
    print("Available seats (marked with a dot):")
    print(PROJECTIONS[projection - 1])
    chosen_seats = []
    for seat in range(tickets):
        seats = input("Choose seat {}>".format(seat + 1))
        seats = tuple(map(int, seats.split(',')))
        while proj.is_free_seat(seats) is None:
            print("Invalid seats - max seat is (10 10)")
            seats = input("Choose seat {}>".format(seat + 1))
            seats = tuple(map(int, seats.split(',')))
        while proj.is_free_seat(seats) is False:
            print("This seat is already taken!")
            seats = input("Choose seat {}>".format(seat + 1))
            seats = tuple(map(int, seats.split(',')))
        with open("settings/reservations.py", "a") as f:
            f.write("    settings.general_settings.PROJECTIONS[{}]. \
reserve_seat({}, {}) # Made by {}\n".format(projection - 1,
                                            seats[0], seats[1],
                                            user))
        chosen_seats.append(seats)
    print("This is your reservation:")
    user_id = get_user_id(user)
    mp_info = get_movie_and_proj_info(movie, projection)
    print("Movie: {} {}".format(mp_info['name'], mp_info['rating']))
    print("Date and Time: {} {} ({})".format(mp_info['date_'],
                                             mp_info['time_'],
                                             mp_info['type']))
    print("Seats: {}".format(chosen_seats))
    end = input("Step 5 (Confirm - type 'finalize')>")
    while end != 'finalize':
        print("TYPE 'finalize' please.")
    finalize(user_id, projection, chosen_seats)
    print("Thanks.")
    logout(user)


def cancel_reservation(username):
    '''
    User cancelling reservation
    '''
    delete_reservations_by_name(username)
    with open('settings/reservations.py', 'r+') as f:
        lines = f.readlines()
    print(lines)
    cprint('How many tickets did you have? ', 'cyan')
    tickets = input()
    lines = lines[::-1]
    for line in range(len(lines)):
        if username in lines[line]:
            for ticket in range(int(tickets)):
                lines.remove(lines[line])
            break
    lines = lines[::-1]
    with open('settings/reservations.py', 'w') as f:
        for line in lines:
            f.write(line)


def exit():
    sys.exit()


def da_help():
    print("show movies - show current movies in the cinema")
    print("show projections - asks for movie id and optional date, \
shows projections for chosen movie")
    print("make reservation - make a reservation in our cinema!")
    print("cancel reservation - cancel your last reservation in our cinema")
    print("exit - log out of our system")
    print("help - what you just clicked")


def main():
    pass


if __name__ == '__main__':
    main()
