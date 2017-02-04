from controllers import (get_teams_in_room, get_teams_for_technology,
                         get_mentor_teams)


def main():
    print(get_teams_in_room("321"))
    print(get_teams_for_technology('Java'))
    get_mentor_teams('Георги Стоянов')


if __name__ == '__main__':
    main()
