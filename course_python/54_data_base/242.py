DB_NAME = "sql_db.db"

# with sqlite3.connect(DB_NAME) as sql:
#     print(sql)
#     print(sqlite3.version)

# with sqlite3.connect(DB_NAME) as sql:
#     sql_req = """CREATE TABLE IF NOT EXISTS courses (
#     id integer PRIMARY KEY,
#     title text NOT NULL,
#     students_qty integer,
#     reviews_qty integer
#     );"""
#     sql.execute(sql_req)

# courses = [
#     (2, "JavaScript course", 0, 0),
#     (3, "Java", 1, 0),
#     (4, "C# course", 0, 0)
# ]

# with sqlite3.connect(DB_NAME) as sql:
#     sql_req = "INSERT INTO courses VALUES (?, ?, ?, ?)"
#     # sql.execute(sql_req, (1, "Python Course", 1, 1))
#     for course in courses:
#         sql.execute(sql_req, course)
#     sql.commit()

# with sqlite3.connect(DB_NAME) as sql:
#     sql_req = "SELECT * FROM courses WHERE students_qty > 0"
#     sql_data = sql.execute(sql_req)
#     for i in sql_data:
#         print(i[1])
#     record = sql_data.fetchall()
#     print(record)


import sqlite3

class Course:
    DB_NAME = "new_data_base_two.db"
    saved_data = []

    def __init__(self):
        self.data_base = self.DB_NAME

    def create_data_base(self):
        with sqlite3.connect(self.data_base) as sql_db:
            sql_req = """CREATE TABLE IF NOT EXISTS my_courses (
            id integer PRIMARY KEY,
            course_name text NOT NULL,
            progress integer
            );"""
            sql_db.execute(sql_req)

    def insert_values(self):
        with sqlite3.connect(self.data_base) as sql_db:
            sql_req = "INSERT INTO my_courses VALUES(?, ?, ?)"
            for i in self.saved_data:
                sql_db.execute(sql_req, i)
            sql_db.commit()

    def get_course_data(self):
        for i in range(1):
            course_id = int(input("Enter course id: "))
            course_title = input("Enter course name: ")
            course_progress = int(input("Enter your porgress: "))
            saved_tuple = (course_id, course_title, course_progress)
            self.saved_data.append(saved_tuple)
        print(self.saved_data)

    def get_db_writes(self):
        with sqlite3.connect(self.data_base) as sql_db:
            sql_req = "SELECT * FROM my_courses"
            sql_data = sql_db.execute(sql_req)
            for i in sql_data:
                print(i)

sql = Course()
sql.create_data_base()
sql.get_course_data()
sql.insert_values()
sql.get_db_writes()
        