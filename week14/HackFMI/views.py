from controllers import (get_teams_in_room, get_teams_for_technology,
                         get_mentor_teams, get_mentor_rooms, get_all_teams)
from prettytable import PrettyTable
from datetime import datetime, timedelta


def convert_time_to_string(time_value):
    needed_time = str(time_value).split(' ')[1].split(':')
    new_time = needed_time[0] + ':' + needed_time[1]
    return new_time


def make_schedule():
    table = PrettyTable(['Hour', 'Team', 'Idea description'])
    table.padding_width = 1
    date = datetime(2017, 2, 5, 19, 30)
    table.add_row([convert_time_to_string(date),
                   'Откриване',
                   'Откриване на хакатона'])
    for team in get_all_teams():
        table.add_row([convert_time_to_string(date + timedelta(minutes=15)),
                       team[0],
                       team[1]])
        date += timedelta(minutes=15)
    return table


def main():
    # print(get_teams_in_room("321"))
    # print(get_teams_for_technology('Java'))
    # get_mentor_teams('Георги Стоянов')
    # print(get_mentor_rooms('Георги Стоянов'))
    print(make_schedule())


if __name__ == '__main__':
    main()
