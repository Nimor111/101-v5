import re


class Panda:

    def __init__(self, name, email, gender):
        self.__validate_name(name)
        self.__validate_gender(gender)
        self.__validate_email(email)

    def __validate_name(self, name):
        if type(name) is not str:
            raise TypeError("NAME MUST BE STRING")
        self.name = name
        return self.name

    def __validate_gender(self, gender):
        if type(gender) is not str and gender not in ['male', 'female']:
            raise TypeError("GENDER MUST BE male OR female")
        self.gender = gender
        return self.gender

    def __validate_email(self, email):
        if not re.match(r'^[A-Za-z0-9\._-]+@[A-Za-z0-9]+\.[A-za-z]*$', email):
            raise ValueError("Not a valid email")
        self.email = email
        return self.email

    def __str__(self):
        return '{}:{}:{}'.format(self.name, self.email, self.gender)

    def __eq__(self, other):
        return self.name == other.name and \
            self.gender == other.gender and \
            self.email == other.email

    def __hash__(self):
        return hash(self.name) + hash(self.gender) + \
            hash(self.email)

    def name(self):
        return self.name

    def gender(self):
        return self.gender

    def email(self):
        return self.email

    def is_male(self):
        return self.gender == 'male'

    def is_female(self):
        return self.gender == 'female'


panda = Panda('Ivo', 'georgi.bojinov@hotmail.com', 'male')
