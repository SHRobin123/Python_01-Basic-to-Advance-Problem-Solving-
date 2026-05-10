#SQLite CRUD Example

import sqlite3

# connect database
conn = sqlite3.connect("students.db")

# create cursor
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# insert data
cursor.execute("INSERT INTO students(name, age) VALUES(?, ?)", ("Robin", 22))

# save changes
conn.commit()

# read data
cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

print("Student Records:")

for row in rows:
    print(row)

# update data
cursor.execute("UPDATE students SET age = ? WHERE name = ?", (23, "Robin"))

conn.commit()

# delete data
cursor.execute("DELETE FROM students WHERE name = ?", ("Robin",))

conn.commit()

# close database
conn.close()

'''
output:-

Student Records:
(1, 'Robin', 22)
'''