# testing.py
# importing the Student and Faculty classes from respective files
from student.main import Student
from faculty.main import Faculty
from crypto.main import *

def test_classes():
	# creating dicts for student and faculty
	student_dict = {'name' : 'John', 'gender': 'Male', 'year': '3'}
	faculty_dict = {'name': 'Emma', 'subject': 'Programming'}

	# creating instances of the Student and Faculty classes
	student = Student(student_dict)
	faculty = Faculty(faculty_dict)

	# getting and printing the student and faculty details
	print(student.get_student_details())
	print()
	print(faculty.get_faculty_details())


def test_func_capitalise():
	assert "Tung nguyen vu ngoc" == capitalise("tung nguyen vu ngoc")
	

def test_func_beautify_name():
	assert "Tung Nguyen Vu Ngoc" == beautify_name("tung nguyen vu ngoc")
