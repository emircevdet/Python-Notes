import sqlite3

class sql_functions:

    def __init__(self):
        self.connection = sqlite3.connect("test_center_system.db")
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""
                            create table if not exists results (
                            id text primary key,
                            name text,
                            score integer,
                            year integer)""")
        self.connection.commit()

    def add_candidate(self, id, name, score, year):
        self.cursor.execute("insert into results values (?,?,?,?)",
                            (id, name, score, year))
        self.connection.commit()

    def list_candidate(self):
        self.cursor.execute("select * from results")
        rows = self.cursor.fetchall()
        for row in rows:
            print("ID: ", row[0])
            print("Name: ", row[1])
            print("Test Score: ", row[2])
            print("Test Year: ", row[3])
            print("-"*30)

    def update_candidate(self, update_id, new_score):
        self.cursor.execute("update results set score = ? where id = ?",
                            (new_score, update_id))
        self.connection.commit()

    def delete_candidate(self, delete_id):
        self.cursor.execute("delete from results where id = ?",
                            (delete_id,))
        self.connection.commit()

    def find_maximum_score(self):
        self.cursor.execute("select *, max(score) from results")
        max_score = self.cursor.fetchone()
        # print(max_score)
        print("Maximum Score:", max_score[2])
        print("Candidate Name:", max_score[1])