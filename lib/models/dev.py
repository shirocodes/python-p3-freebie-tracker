from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

from .base import Base
from .association import company_dev

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String(), nullable=False)
    
    freebies = relationship('Freebie', backref=backref('dev'), cascade='all, delete-orphan')
    companies = relationship('Company', secondary=company_dev, back_populates='devs')

    def __repr__(self):
        return (
            f'Dev(id={self.id},'
            f'name={self.name})'
        )
    
    def received_one(self, item_name:str) -> bool:
        """
        Checks if a dev has a freebie with the indicated item name.
        """
        return any(freebie.item_name == item_name for freebie in self.freebies)
      
    def give_away(self, dev, freebie):  
        """
        if a dev already owns a certain freebie, this method allows the dev
        to transfer such a freebie to another dev.
        """
        if freebie in self.freebies:
            freebie.dev = dev
            return freebie
        else:
            raise ValueError(f"{self.name} does not own this freebie.")
            
    
    