
import xml.etree.ElementTree as ET

# Parse the XML document
tree = ET.parse("students.xml")

# Get the root element
root = tree.getroot()

# Display student details
print("STUDENT DETAILS")
print("----------------------------")

for student in root.findall("student"):

    rollno = student.find("rollno").text
    name = student.find("name").text
    branch = student.find("branch").text
    marks = student.find("marks").text

    print("Roll Number:", rollno)
    print("Name:", name)
    print("Branch:", branch)
    print("Marks:", marks)
    print("----------------------------")
