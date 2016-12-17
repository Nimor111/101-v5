from create_database import *
from users import User, Doctor


class Menu:
    def __init__(self, name):  # hospital name cus why not
        self.menu = None
        self.name = name
        # self.commands = {'1': self.login(), '2': self.register(),
        # '3': self.help(), '4': self.exit()}

    def welcome_screen(self):
        self.menu = '''
        Welcome to {}!
        Choose:
        1 To log into the system,
        2 to register as a new user,
        3 for help main,
        4 to exit the system.
        '''.format(self.name)
        return self.menu

    def enter_user(self):
        print('> username: ')
        username = input()
        password = getpass.getpass('> password: ')
        print('> age: ')
        age = input()
        print('> gender (optional): ')
        gender = input()
        user = User()
        if user.init_components(username, password, age, gender):
            insert_user(user)
            return user
        self.enter_user()

    def run(self):
        pass


def main():
    # create_and_fill_data()
    menu = Menu('Hospital Manager')
    # print(menu.welcome_screen())
    user = menu.enter_user()
    # print(user)
    # doctor = Doctor()
    # doctor.init_components('Pesho', 'Pesho1234567', 24, 'M', 'surgeon')
    # print(doctor)
    promote_to_doctor(user, 'professor')


if __name__ == '__main__':
    main()
