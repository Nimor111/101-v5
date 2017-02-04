from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()
engine = create_engine('sqlite:///test.db')

Session = sessionmaker(bind=engine)

session = Session()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship(User, backref=backref('posts', uselist=True))


def main():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    john = User(name="John")
    post1 = Post(owner=john)
    post2 = Post(owner=john)
    session.add(post1)
    session.add(post2)
    session.commit()
    session.refresh(john)
    import ipdb; ipdb.set_trace()


if __name__ == '__main__':
    main()
