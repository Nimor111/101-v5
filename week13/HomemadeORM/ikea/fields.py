class BaseColumn:

    def transform(self, data):
        return str(data)

    def validate(self, value):
        return True


class PKColumn(BaseColumn):

    def transform(self, value):
        return int(value)


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

    def transform(self, value):
        return int(value)

    def validate(self, value):
        if value < 0:
            return False
        return True
