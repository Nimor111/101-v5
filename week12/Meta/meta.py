from datetime import datetime
import json

from fields import Field, EmailField, CharField, DateTimeField


class SerializerMeta(type):
    def __new__(cls, name, bases, clsdict):
        fields = {}

        for attr, value in clsdict.items():
            if isinstance(value, Field):
                fields[attr] = value

        for attr, _ in fields.items():
            clsdict.pop(attr)

        clsdict['_fields'] = fields

        return super().__new__(cls, name, bases, clsdict)


class Serializer(metaclass=SerializerMeta):
    def __init__(self, obj):
        self._obj = obj
        self._is_validation_called = False

    def is_valid(self):
        valid = True

        for field_name, field in self._fields.items():
            print(field_name)
            print(field)
            if not field.validate(getattr(self._obj, field_name)):
                valid = False
                break

        self._is_validation_called = True
        return valid

    @property
    def data(self):
        if not self._is_validation_called:
            raise Exception("Must call is_valid first!")

        return json.dumps({field_name: field.transform(
                          getattr(self._obj, field_name))
            for field_name, field in self._fields.items()}, indent=4)


class Comment(object):
    def __init__(self, email, content, created_at=None):
        self.email = email
        self.content = content

        if created_at is None:
            created_at = datetime.now()

        self.created_at = created_at


class CommentSerializer(Serializer):
    email = EmailField()
    content = CharField()
    created_at = DateTimeField()


def main():
    comment = Comment(email="metaclasseslol@pesho.com",
                      content="Sesh se obache")
    serializer = CommentSerializer(comment)
    print(serializer.is_valid())
    print(serializer.data)


if __name__ == '__main__':
    main()
