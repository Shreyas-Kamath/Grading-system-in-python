#imports
import student as s

#actual
print("Enter a file to analyse:")
filename = input()

students = s.read(filename)
s.write(students)
s.generate_reports(students)
