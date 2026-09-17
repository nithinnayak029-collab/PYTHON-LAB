import sqlite3

# Connect to SQLite database
con = sqlite3.connect("student.db")
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    cgpa REAL NOT NULL
)
""")
con.commit()


# Add student
def add_student():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    cgpa = float(input("Enter CGPA: "))

    cur.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                (roll, name, dept, cgpa))
    con.commit()
    print("Student added successfully.")


# Display students
def display_students():
    cur.execute("SELECT * FROM students")
    records = cur.fetchall()

    print("\n--- Student Details ---")
    for s in records:
        print("Roll No:", s[0])
        print("Name:", s[1])
        print("Department:", s[2])
        print("CGPA:", s[3])
        print("-----------------------")


# Search student
def search_student():
    roll = int(input("Enter Roll No: "))

    cur.execute("SELECT * FROM students WHERE roll_no=?", (roll,))
    s = cur.fetchone()

    if s:
        print("\nRoll No:", s[0])
        print("Name:", s[1])
        print("Department:", s[2])
        print("CGPA:", s[3])
    else:
        print("Student not found.")


# Main menu
while True:
    print("\n===== Student Information System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")

con.close()
