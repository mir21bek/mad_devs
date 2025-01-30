from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):
    __tablename__ = 't_users'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    access_token = Column(String(255), nullable=False)
    roles = Column(String(255), nullable=False)
    diagnoses = relationship("Diagnose", back_populates="user")


class Role(Base):
    __tablename__ = 't_roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('t_users.id'), nullable=False)
    user = relationship('User', back_populates='roles')


class Diagnose(Base):
    __tablename__ = 't_diagnoses'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('t_users.id'), nullable=False)
    user = relationship('User', back_populates='diagnoses')
