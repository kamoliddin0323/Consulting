from sqlalchemy import Column, Integer, String,Float
from database import Base

class UserData(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True)
    username = Column(String, index=True)
    full_name = Column(String)
    birthdate = Column(String)
    location = Column(String)
    phone = Column(String)
    study_year = Column(String)
    degree = Column(String)
    certificate = Column(String)
    score = Column(Float)  

    def __repr__(self):
        return f"<UserData(user_id={self.user_id}, username={self.username}, full_name={self.full_name})>"
