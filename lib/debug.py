#!/usr/bin/env python3

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # queries
    all_companies = session.query(Company).all()
    all_devs = session.query(Dev).all()
    
    def create_dev(session, dev_name):
        """
        create and persist a new dev in database
        """
        new_dev = Dev(name=dev_name)
        session.add(new_dev)
        session.commit()
        return new_dev
    
    def update_freebie_value(session, freebie_id, new_value):
        """
        Update a certain freebie's value
        """
        freebie = session.query(Freebie).get(freebie_id)
        if freebie:
            freebie.value = new_value
            session.commit()
        return freebie
    
    def delete_dev(session, dev_id):
        """
        Delete a dev, and due to cascade, freebies should also be removed
        """
        dev = session.query(Dev).get(dev_id)
        if dev:
            session.delete(dev)
            session.commit()
            return f"Deleted developer {dev.name}"
        return "Developer not found"
    
    def get_freebies_by_desc_value(session):
        """
        return all freebies sorted in a descending manner
        """
        return session.query(Freebie).order_by(Freebie.value.desc()).all()
    
    def get_freebies_by_value(session, max_value):
        """
        returning freebies based on a particular value.
        for instance: get_freebies_by_value(50)
        """
        return session.query(Freebie).filter(Freebie.value < max_value).all()
    
    def companies_with_several_freebies(session):
        """
        returning companies giving out more than 2 of the same freebie.
        Begins by grouping by company and item name and counting, then
        extracting company_ids from results to query.
        """
        results = (
            session.query(Freebie.company_id, Freebie.item_name,
            func.count(Freebie.id).label('counts'))
            .group_by(Freebie.company_id, Freebie.item_name)
            .having(func.count(Freebie.id) >= 2)
            .all()
        )
        
        company_ids = set([result.company_id for result in results])
        return session.query(Company).filter(Company.id.in_(company_ids)).all()
    
    def get_devs_with_this_freebie(session, item_name):
        """
        Returns all devs who own a certain freebie
        """  
        return (
            session.query(Dev).join(Dev.freebies)
            .filter(Freebie.item_name == item_name)
            .distinct().all()
        )
        
    def devs_owning_costly_freebies(session, min_value):
       """
       returns devs with freebies worth more than stated value
       """ 
       return (
        session.query(Dev).join(Dev.freebies)
        .filter(Freebie.value > min_value).distinct().all()
       )
       
     
    import pdb; pdb.set_trace()
