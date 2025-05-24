from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from .base import Base
from .association import company_dev

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    founding_year = Column(Integer(), nullable=False)
    
    freebies = relationship('Freebie', backref=backref('company'))
    devs = relationship('Dev', secondary=company_dev, back_populates='companies')
    
    def __repr__(self):
        return f'<Company {self.name}>'
