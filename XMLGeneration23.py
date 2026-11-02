
import xml.etree.ElementTree as ET

# Create root element
root = ET.Element("students")

# Function to add student
def add_student(roll, name, branch, marks):
    student = ET.SubElement(root, "student")

    ET.SubElement(student, "rollno").text = str(roll)
    ET.SubElement(student, "name").text = name
    ET.SubElement(student, "branch").text = branch
    ET.SubElement(student, "marks").text = str(marks)

# Add student records
add_student(101, "Nithin", "CSE", 85)
add_student(102, "Rahul", "ECE", 90)
add_student(103, "Arjun", "ME", 78)

# Modify student details
for student in root.findall("student"):
    if student.find("rollno").text == "102":
        student.find("name").text = "Rahul Kumar"
        student.find("marks").text = "95"

# Delete a student record
for student in root.findall("student"):
    if student.find("rollno").text == "103":
        root.remove(student)
        break

# Generate XML tree
tree = ET.ElementTree(root)

# Save XML document
ET.indent(tree, space="    ")
tree.write("students.xml", encoding="utf-8", xml_declaration=True)

print("XML document created and modified successfully!")

# Display updated student information
print("\nUPDATED STUDENT DETAILS")

for student in root.findall("student"):
    print("Roll No:", student.find("rollno").text)
    print("Name:", student.find("name").text)
    print("Branch:", student.find("branch").text)
    print("Marks:", student.find("marks").text)
    print("----------------------")