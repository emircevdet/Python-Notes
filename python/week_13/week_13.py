# import sqlite3, Faker
# CREATE TABLE (IF NOT EXISTS)
# INSERT INTO (single, multiple)
# SELECT (all, particular columns, WHERE)
# UPDATE
# DELETE

import sqlite3
from faker import Faker

fake = Faker()

connection = sqlite3.connect("test_center.db")
cursor = connection.cursor()

# to ignore duplicate values (there may be a better solution)
# cursor.execute("drop table if exists results")

def create_table():
    # CREATE TABLE
    cursor.execute("""
                   create table if not exists results (
                   id text primary key,
                   name text,
                   score integer,
                   year integer)""")
    connection.commit()

def insert_single():
    # INSERT A SINGLE RECORD
    candidate1 = (fake.passport_number(), 
                fake.name(), 
                fake.random_int(0, 100), 
                fake.random_int(2001, 2025))

    cursor.execute("insert into results (id, name, score, year) values (?,?,?,?)", 
                   candidate1)
    connection.commit()

    candidate2 = (fake.passport_number(), 
                fake.name(), 
                fake.random_int(0, 100), 
                fake.random_int(2001, 2025))

    cursor.execute("insert into results (id, name, score, year) values (?,?,?,?)", 
                   candidate2)
    connection.commit()
    
def insert_multiple():
    # INSERT MULTIPLE RECORD
    new_candidates = [
        (fake.passport_number(), fake.name(), fake.random_int(0, 100), fake.random_int(2001, 2025)),
        (fake.passport_number(), fake.name(), fake.random_int(0, 100), fake.random_int(2001, 2025)),
        (fake.passport_number(), fake.name(), fake.random_int(0, 100), fake.random_int(2001, 2025)),
    ]
    # insert_query = "insert into results values (?,?,?,?)"
    # cursor.executemany(insert_query, new_candidates)

    candidates = [(fake.passport_number(), fake.name(), fake.random_int(0, 100), fake.random_int(2001, 2025)) for _ in range(3)]
    insert_query = "insert into results values (?,?,?,?)"
    cursor.executemany(insert_query, candidates)
    connection.commit()

def insert_with_keyboard():
    candidate_id = input("Passport number: ")
    candidate_name = input("Name:")
    test_score = int(input("Score: "))
    test_year = int(input("Year: "))
    cursor.execute("insert into results values (?,?,?,?)", 
                   (candidate_id, candidate_name, test_score, test_year))
    connection.commit()

def select_value():
    # SELECT
    cursor.execute("select * from results")
    # cursor.execute("select name, score from results")
    # cursor.execute("select name, score from results where score >= 85")
    rows = cursor.fetchall()

    print(type(rows))
    print(rows)

    for row in rows:
        print(row)

def update_value():
    # UPDATE
    cursor.execute("update results set score = 100 where name = 'James Clear'")
    connection.commit()

def delete_value():
    # DELETE
    cursor.execute("delete from results where score < 50")
    # cursor.execute("delete from results")
    connection.commit()

create_table()
insert_single()
# insert_multiple()
# insert_with_keyboard()
# select_value()
# update_value()
# delete_value()

# all these functions can be selected via a menu

# saves (commits) the changes to the database
# connection.commit()
connection.close()


