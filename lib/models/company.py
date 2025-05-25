from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref, Session

from .base import Base
from .association import company_dev

class Company(Base):
    """
    In Hackathons, a company gives out freebies to developers.
    Company has a one-to-many relationship with Freebie.
    Has a many-to-many relationships with Dev
    """
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    founding_year = Column(Integer(), nullable=False)
    
    freebies = relationship('Freebie', backref=backref('company'), cascade='all, delete-orphan')
    devs = relationship('Dev', secondary=company_dev, back_populates='companies')
    
    def __repr__(self):
        return (
            f'Company(id={self.id},'
            f'name={self.name},'
            f'founding_year={self.founding_year})'
        )
    
    def give_freebie(self, dev, item_name, value):
        from .freebie import Freebie
        return Freebie(item_name=item_name, value=value,
                       company=self, dev=dev
                       )
    
    @classmethod
    def oldest_company(cls, session: Session):
        return session.query(cls).order_by(cls.founding_year).first()
        
