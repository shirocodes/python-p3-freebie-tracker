#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

from faker import Faker
import random

# defining database connection 
if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # initializing faker
    fake = Faker()

    # creating instances

    companies = []
    for _ in range(7):
        company = Company(
            name=fake.company(),
            founding_year=random.randint(2000,2023)
        )
        companies.append(company)
    session.add_all(companies)
    session.commit()

    devs = []
    for _ in range(7):
        dev = Dev(
            name=fake.name()
        )
        devs.append(dev)
    session.add_all(devs)
    session.commit()

    # linking companies and devs many-to-many relationships
    for dev in devs:
        associated_companies = random.sample(companies, random.randint(1,6))
        for company in associated_companies:
            dev.companies.append(company)
    session.commit()

    # freebies has-manys
    freebies = []
    item_names = ['Pens', 'Tshirts', 'Uber-discounts', 'Notebook', 'stickers']
    for _ in range(10):
        freebie = Freebie(
            item_name=random.choice(item_names),
            value=random.randint(1,100),
            company=random.choice(companies),
            dev=random.choice(devs)
        )
        freebies.append(freebie)
    session.add_all(freebies)
    session.commit()

    print("successfuly seeded database!")


