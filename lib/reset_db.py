#!/usr/bin/env python3

import os
import subprocess

DB_PATH = 'freebies.db'

def delete_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Deleted old database: {DB_PATH}")
    else:
        print(f"No available database at {DB_PATH}")

def run_migration():
    print("Running alembic migrations ...")
    subprocess.run(["alembic", "upgrade", "head"], check=True)
    print("database schema migrated")
        
def seed_db():
    print("seeding the database...")
    subprocess.run(["python3", "seed.py"], check=True)
    print("Seeded database.")

if __name__ == '__main__':
    delete_db()
    run_migration()
    seed_db()
    print("Reset complet! begin quering")