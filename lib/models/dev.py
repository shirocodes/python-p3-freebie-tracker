from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from .base import Base
from .association import company_dev

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String(), nullable=False)
    
    freebies = relationship('Freebie', backref=backref('dev'))
    companies = relationship('Company', secondary=company_dev, back_populates='devs')

    def __repr__(self):
        return f'<Dev {self.name}>'