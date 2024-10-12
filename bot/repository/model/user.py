from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a new base class for declarative class definitions
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    tg_user_id = Column(Integer, primary_key=True, autoincrement=True)
    role = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(id={self.tg_user_id}, role='{self.role}')>"
