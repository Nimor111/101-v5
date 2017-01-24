class BaseColumn:

    def set_data(self, data):
        print("EXECUTING")


class PKColumn(BaseColumn):
    pass


class TextColumn(BaseColumn):

    def __init__(self, max_length=100):
        self.max_length = max_length

    def transform(self, value):
        return str(value)

    def validate(self, value):
        if len(value) > self.max_length:
            return False
        return True


class IntegerColumn(BaseColumn):

    def __init__(self, number=20):
        self.number = number

    def validate(self, value):
        if value < 0:
            return False
        return True
