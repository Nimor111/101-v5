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


# Creating all tables from BaseModel class
# BaseModel.create_all_tables()

def main():
    BaseModel.create_all_tables()
    print(User.create_obj(name="Pesho", age=22).name)
    print(Student.create_obj(email="Pesho", shirt_size=1).email)


if __name__ == '__main__':
    main()


# Create record in table
# User.create_obj(name="Rosi", age=22)

# Return dict with object
# User.filter(name="Panda")
