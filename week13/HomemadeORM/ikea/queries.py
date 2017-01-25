from ikea.models import BaseModel
from ikea.fields import IntegerColumn, PKColumn, TextColumn
from collections import OrderedDict


class User(BaseModel):
    __tablename__ = 'users'

    id_ = PKColumn()
    name = TextColumn(max_length=100)
    age = IntegerColumn(number=20)


def create_table(obj):
    query = "CREATE TABLE IF NOT EXISTS {} (\n" \
            .format(obj.__tablename__.upper())

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


def main():
    print(create_table(User))


if __name__ == '__main__':
    main()
