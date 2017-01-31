from ikea.models import BaseModel
from ikea.fields import PKColumn, IntegerColumn, TextColumn


class User(BaseModel):
    __tablename__ = 'users'

    id_ = PKColumn()
    name = TextColumn(max_length=100)
    age = IntegerColumn(number=20)


class Student(User):
    __tablename__ = 'students'

    email = TextColumn()
    shirt_size = IntegerColumn(number=1)


def main():
    # BaseModel.drop_tables()
    BaseModel.create_all_tables()
    User.create_obj(name="Evi", age=20)
    User.create_obj(name="Evi", age=22)
    User.create_obj(name="Evi", age=24)
    # u = User()
    # s = Student()
    # import ipdb; ipdb.set_trace()


if __name__ == '__main__':
    main()


# Create record in table
# User.create_obj(name="Rosi", age=22)

# Return dict with object
# User.filter(name="Panda")
