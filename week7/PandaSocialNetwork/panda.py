import re


class Panda:

    def __init__(self, name, email, gender):
        self.__validate_name(name)
        self.__validate_gender(gender)
        self.__validate_email(email)

    def __validate_name(self, name):
        if type(name) is not str:
            raise TypeError("NAME MUST BE STRING")
        self.__name = name
        return self.__name

    def __validate_gender(self, gender):
        if type(gender) is not str and gender not in ['male', 'female']:
            raise TypeError("GENDER MUST BE male OR female")
        self.__gender = gender
        return self.__gender

    def __validate_email(self, email):
        if not re.match(r'^[A-Za-z0-9\._-]+@[A-Za-z0-9]+\.[A-za-z]*$', email):
            raise ValueError("Not a valid email")
        self.__email = email
        return self.__email

    def __str__(self):
        return '{}:{}:{}'.format(self.name, self.email, self.gender)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__name == other.__name and \
            self.__gender == other.__gender and \
            self.__email == other.__email

    def __hash__(self):
        return hash(self.__email)

    def name(self):
        return self.__name

    def gender(self):
        return self.__gender

    def email(self):
        return self.__email

    def isMale(self):
        return self.__gender == 'male'

    def isFemale(self):
        return self.__gender == 'female'


panda = Panda('Ivo', 'georgi.bojinov@hotmail.com', 'male')