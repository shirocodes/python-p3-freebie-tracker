from sqlalchemy import Column, Integer, String, ForeignKey
from .base import Base

class Freebie(Base):
    __tablename__ = 'freebies'
    
    id = Column(Integer(), primary_key=True)
    item_name = Column(String(), nullable=False)
    value = Column(Integer(), nullable=False)
    company_id = Column(Integer(), ForeignKey('companies.id'), nullable=False)
    dev_id = Column(Integer(), ForeignKey('devs.id'), nullable=False)
    
    def __repr__(self):
        return (
            f'Freebie(id={self.id},'
            f'item_name={self.item_name},'
            f'value={self.value})'
            )
    
    def print_details(self):
           return f'{self.dev.name} owns a {self.item_name} from {self.company.name}'
    