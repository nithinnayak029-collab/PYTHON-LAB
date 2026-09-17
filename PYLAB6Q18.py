import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary,REAL
)
""")

n = int(input("Enter number of employees : "))

for i in range(n):
    id = int(input("Enter employee I'd:"))
    name = input("Enter employee name : ")
    department = input("Enter department : ")
    salary = float(input("Enter salary : "))

    cursor.execute("""
    INSERT INTO employee VALUES(?,?,?,?)
    """,(id,name,department,salary))

conn.commit()

dept = input("\nEnter department to generate repport : ")

cursor.execute("""
SELECT name,salary
FROM employee
WHERE department = ?
""",(dept))

print("\nDepartment-wise Salary Rerport ")
print('------------------------------')

rows = cursor.fetchall()

for row in rows : 
    print("Name : ",row[0], "Salary : ",row[1])

conn.close()