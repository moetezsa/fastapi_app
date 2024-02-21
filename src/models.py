import sqlalchemy as sql
from src import database


class Student(database.Base):
    __tablename__ = "Students"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    first_name = sql.Column(sql.String)
    last_name = sql.Column(sql.String)
    date_of_birth = sql.Column(sql.DateTime)
    age = sql.Column(sql.Integer)
