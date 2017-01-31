from ikea.fields import IntegerColumn, PKColumn, TextColumn
from collections import OrderedDict


def create_table(obj):
    query = "CREATE TABLE IF NOT EXISTS {} (\n" \
            .format(obj.__tablename__)

    fields = obj.fields
    field_types = OrderedDict()
    for key, value in fields.items():
        if type(value) == IntegerColumn:
            field_types['IntegerColumn'] = 'INTEGER NOT NULL'
        if type(value) == TextColumn:
            field_types['TextColumn'] = 'TEXT NOT NULL'
    field_names = []
    for key, value in fields.items():
        if key != 'id_':
            field_names.append(key.upper())

    query += '  ID INTEGER PRIMARY KEY AUTOINCREMENT,\n'
    for i in range(len(field_names)):
        if i != len(field_names) - 1:
            query += '  {} {},\n'.format(field_names[i],
                                         list(field_types.values())[i])
        else:
            query += '  {} {}\n'.format(field_names[i],
                                        list(field_types.values())[i])

    query += (')')

    return query


def insert(classname, *args, **kwargs):
    query = "INSERT INTO {} (".format(classname.__tablename__.upper())
    key_vals = list(kwargs.keys())
    vals = list(kwargs.values())
    for key in range(len(key_vals)):
        if key == len(key_vals) - 1:
            query += "{})".format(key_vals[key].upper())
        else:
            query += "{}, ".format(key_vals[key].upper())
    query += "\nVALUES("
    for key, _ in kwargs.items():
        if key == list(kwargs.keys())[-1]:
            query += "?"
        else:
            query += "?, "
    query += ")"
    return query


def drop(classname):
    query = "DROP TABLE IF EXISTS {}".format(classname.__tablename__)
    return query


class User():
    __tablename__ = 'users'

    id_ = PKColumn()
    name = TextColumn(max_length=100)
    age = IntegerColumn(number=20)


def main():
    print(insert(User, name="Evi", age=20))


if __name__ == '__main__':
    main()
