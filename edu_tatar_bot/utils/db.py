from sqlalchemy import Column, DateTime, String, Integer, create_engine, Float, Boolean, BigInteger, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relation
import datetime
from configparser import ConfigParser

config = ConfigParser()
config.read('config/config.ini')

engine = create_engine(
    f'{config["database"]["protocol"]}{config["database"]["host"]}'
)

session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = session.query_property()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    chat_id = Column(BigInteger, unique=True)
    username = Column(String)
    fullname = Column(String)
    date_join = Column(DateTime, default=datetime.datetime.now())

    edu_tatar = relation("EduTatarUser", back_populates='user')


class EduTatarUser(Base):
    __tablename__ = 'edu_tatar_users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relation("User")

    login = Column(String)
    password = Column(String)
    name = Column(String)
    school = Column(String)
    grade = Column(String)

    marks_amount = Column(Integer, default=0)
    total_gpa = Column(Integer, default=0)

    date_changed = Column(DateTime, default=datetime.datetime.now())


Base.metadata.create_all(bind=engine)
