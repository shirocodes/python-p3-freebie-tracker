from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

# Associations table => many-to-many relationship
company_dev = Table(
    'company_dev',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('companies.id'), primary_key=True),
    Column('dev_id', Integer, ForeignKey('devs.id'), primary_key=True)
)