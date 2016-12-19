from create_database import *
from modify_database import *
from users import User, Doctor, Patient
from queries import SELECT_SPECIFIC_DOCTOR
import getpass
from password import encode_pass
import sys
import os


class Menu:
    def __init__(self, name):  # hospital name cus why not
        self.name = name

    def welcome_screen(self):
        print('''Welcome to {}!
        Choose:
        1 To log into the system,
        2 to register as a new user,
        3 for help main,
        4 to exit the system.
        '''.format(self.name))

    def register(self):
        print('> username: ')
        username = input()
        password = getpass.getpass('> password: ')
        new_pass = getpass.getpass('> password again: ')
        while new_pass != password:
            print('Passwords don\'t match.')
            new_pass = getpass.getpass('> password again: ')
        print('> age: ')
        age = input()
        print('> gender (optional): ')
        gender = input()
        user = User()
        if user.init_components(username, password, age, gender):
            insert_user(user)
            Menu.__doc_promotion(user)
            Menu.__patient_promotion(user)
        self.register()

    @staticmethod
    def __doc_promotion(user):
        if 'Dr.' in user.username:
            print('> academic_title: ')
            academic_title = input()
            promote_to_doctor(user, academic_title)

    @staticmethod
    def __patient_promotion(user):
        if 'Dr' not in user.username:
            c.execute(SELECT_DOCTOR_NAME)
            doctors = c.fetchall()
            print('choose a doctor to cure your diseases: ')
            i = 0
            for doctor in doctors:
                i += 1
                print("{}) {}, {}".format(i, doctor['username'],
                                          doctor['academic_title']))
            doctor = input()
            promote_to_patient(user, doctor)

    def login(self):
        print('> username: ')
        username = input()
        password = getpass.getpass('> password: ')
        c.execute(SELECT_USERS)
        users = c.fetchall()

        for user in users:
            if username == user['username']:
                if encode_pass(password) == user['password']:
                    c.execute(UPDATE_LOGIN, (user['id'], ))
                    db.commit()
                    if 'Dr.' in user['username']:
                        c.execute(SELECT_DOCTOR_NAME)
                        doctor = c.fetchone()
                        self.doctor_login(user['username'],
                                          doctor['academic_title'])
                    else:
                        self.patient_login(user['username'])

    def patient_login(self, username):
        while True:
            print('''
            Hi, {},
            You are a patient in {}.
            You have the abilities to:
            1) See the free hours of your doctor
            2) Reserve hour for visitation
            3) Stay at the hospital for an injury
            4) See the academic title of your doctor
            5) List your hospital stays
            6) Change your doctor
            7) Change your username and/or age
            8) log out'''.format(username, self.name))
            command = input('> ')
            os.system('clear')
            if command == '1':
                print(self.__get_visitation_hours(username))
            elif command == '7':
                self.__update_username_and_age(username)
            elif command == '5':
                self.__view_hospital_stays(username)
            elif command == '3':
                self.__add_hospital_stay(username)
            elif command == '4':
                self.__academic_title(username)
            elif command == '2':
                self.__reserve_visitation(username)
            elif command == '8':
                self.__logout(username)
            elif command == '6':
                self.__update_doctor(username)
            else:
                break

    def doctor_login(self, username, academic_title):
        while True:
            print('''
            Hi, {},
            You are a {} doctor in {}.
            You have the abilities to:
            1) List all of your patients
            2) Add hours for visitation
            3) Delete free hours of visitation
            4) See the room and the duraiton of the hospital stays for each of
            your patients
            5) Change your username and/or age
            6) Umm...
            7) log out'''.format(username, academic_title, self.name))
            command = input('> ')
            os.system('clear')
            if command == '1':
                self.__get_doctor_patients(username)
            elif command == '2':
                self.__update_visitation_hours(username)
            elif command == '3':
                self.__delete_visitation_hours(username)
            elif command == '4':
                self.__get_room_and_duration(username)
            elif command == '5':
                self.__update_username_and_age(username)
            elif command == '7':
                self.__logout(username)
            else:
                break

    def help(self):
        print('TODO')

    def exit(self):
        sys.exit()

    def __logout(self, username):
        c.execute(SELECT_USERS)
        users = c.fetchall()

        for user in users:
            if username == user['username']:
                c.execute(UPDATE_LOGOUT, (username, ))
                db.commit()
        self.exit()

    def __reserve_visitation(self, username):
        starthour = input('> starthour: ')
        add_visitation(username, starthour)

    def __academic_title(self, username):
        title = get_academic_title(username)
        print('{}, your doctor is of title {}.'
              .format(username,
                      title['academic_title']))

    def __add_hospital_stay(self, username):
        startdate = input('> start date ')
        enddate = input('> end date ')
        injury = input('> injury ')
        add_hospital_stay(username, injury, startdate, enddate)

    def __view_hospital_stays(self, username):
        hospital_stays = view_hospital_stays(username)
        if hospital_stays:
            for stay in hospital_stays:
                print("Stay on {} in room {} with {}.".format(stay[0],
                                                              stay[1],
                                                              stay[2]))
        else:
            print("You have no current or past stays : Congratulations!")

    def __update_username_and_age(self, username):
        new_username = input('> new username: ')
        new_age = input('> new age: ')
        update_username_and_age(username, new_username, new_age)

    def __update_doctor(self, username):
        c.execute(SELECT_DOCTOR_NAME)
        doctors = c.fetchall()
        print('choose a doctor to cure your diseases: ')
        i = 0
        for doctor in doctors:
            i += 1
            print("{}) {}, {}".format(i, doctor['username'],
                                      doctor['academic_title']))
        doctor = input()
        update_patient_doctor(username, doctor)

    def __get_visitation_hours(self, username):
        return get_visitation_hours(username)

    def __get_doctor_patients(self, username):
        get_doctor_patients(username)

    def __update_visitation_hours(self, username):
        hours = input('> visitation hours? (format hh:mm - hh:mm) ')
        update_visitation_hours(username, hours)

    def __delete_visitation_hours(self, username):
        delete_visitation_hours(username)

    def __get_room_and_duration(self, username):
        get_rooms_and_duration(username)


def main():
    # create_and_fill_data()
    menu = Menu('Hospital Manager')
    menu.welcome_screen()
    command = input('> ')
    dict = {'1': menu.login}
    while True:
        if command == '1':
            dict['1']()
            # menu.login()
        elif command == '2':
            menu.register()
        elif command == '3':
            menu.help()
            menu.welcome_screen()
            command = input('> ')
        elif command == '4':
            menu.exit()


if __name__ == '__main__':
    main()
