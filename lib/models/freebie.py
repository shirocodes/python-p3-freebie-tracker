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
        dev_name = self.dev.name if self.dev else "unknown Dev"
        company_name = self.company.name if self.company else "unknown Company"
        return f"<{dev_name} owns a {self.item_name} from {company_name}>"