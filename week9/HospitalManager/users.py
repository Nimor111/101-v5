from password import encode_pass, validate_pass


class User:
    def __init__(self):
        self.username = None
        self.password = None
        self.age = None
        self.gender = None

    def init_components(self, username, password, age, gender=None):
        self.username = username
        if self.__validate_password(password):
            self.password = encode_pass(password)
        else:
            print("Incorrect password! Input again. Must have 1 uppercase \
                    1 lowercase letter, 1 digit and be longer than 7 symbols")
            return False
        self.age = age
        if self.__validate_gender(gender):
            self.gender = gender
        return True

    def __str__(self):
        return '{} -> {} -> {} -> {}'.format(self.username, self.password,
                                             self.age, self.gender)

    def __repr__(self):
        return self.__str__()

    def __validate_password(self, name):
        return validate_pass(name)

    def __validate_gender(self, gender):
        if gender != 'F' and gender != 'M':
            return False
        return True


class Doctor(User):

    def __init__(self):
        super().__init__()

    def init_components(self, academic_title):
        self.academic_title = academic_title

    def __str__(self):
        return super().__str__() + '->{}'.format(self.academic_title)

    def __repr__(self):
        return self.__str__()


class Patient(User):
    pass
