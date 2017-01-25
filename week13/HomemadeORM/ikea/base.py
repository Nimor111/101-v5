from ikea.fields import BaseColumn
from collections import OrderedDict


class Metabase(type):

    def __new__(cls, name, bases, clsdict):
        fields = OrderedDict()
        clsobj = super().__new__(cls, name, bases, clsdict)

        if not hasattr(clsobj, '__tablename__'):
            raise AttributeError("Models must have a __tablename__!")

        if not hasattr(clsobj, '_registry'):
            clsobj._registry = set()
        else:
            clsobj._registry.add(clsobj)

        for attr, value in clsdict.items():
            if isinstance(value, BaseColumn):
                fields[attr] = value

        for attr, _ in fields.items():
            clsdict.pop(attr)

        setattr(clsobj, 'fields', fields)

        return clsobj


def main():
    pass


if __name__ == '__main__':
    main()
