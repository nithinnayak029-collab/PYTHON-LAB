import sqlite3

con = sqlite3.connect("employee.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS employee(
id INTEGER PRIMARY KEY,
name TEXT,
designation TEXT,
department TEXT,
salary REAL)""")

def add():
    data = input("Enter ID, Name, Designation, Department, Salary: ").split(",")
    cur.execute("INSERT INTO employee VALUES(?,?,?,?,?)", data)
    con.commit()
    print("Employee added.")

def view():
    cur.execute("SELECT * FROM employee")
    for row in cur.fetchall():
        print(row)

def update():
    id = input("Enter Employee ID: ")
    salary = input("Enter new salary: ")
    cur.execute("UPDATE employee SET salary=? WHERE id=?", (salary, id))
    con.commit()
    print("Employee updated.")

def delete():
    id = input("Enter Employee ID: ")
    cur.execute("DELETE FROM employee WHERE id=?", (id,))
    con.commit()
    print("Employee deleted.")

while True:
    print("\n1.Add  2.View  3.Update  4.Delete  5.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        add()
    elif ch == "2":
        view()
    elif ch == "3":
        update()
    elif ch == "4":
        delete()
    elif ch == "5":
        break
    else:
        print("Invalid choice")

con.close()
