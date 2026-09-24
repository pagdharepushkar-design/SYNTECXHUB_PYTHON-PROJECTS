
import json


class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        grade = input("Enter student grade: ")

        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists!")
                return

        student = Student(name, student_id, grade)
        self.students.append(student)

        self.save_students()
        print("Student added successfully!")

    def list_students(self):
        if len(self.students) == 0:
            print("No students found.")
            return

        print("\n===== STUDENT LIST =====")

        for student in self.students:
            print("ID:", student.student_id)
            print("Name:", student.name)
            print("Grade:", student.grade)
            print("------------------------")

    def update_student(self):
        student_id = input("Enter student ID to update: ")

        for student in self.students:
            if student.student_id == student_id:

                name = input("Enter new name: ")
                grade = input("Enter new grade: ")

                if name != "":
                    student.name = name

                if grade != "":
                    student.grade = grade

                self.save_students()
                print("Student updated successfully!")
                return

        print("Student not found!")

    def delete_student(self):
        student_id = input("Enter student ID to delete: ")

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_students()
                print("Student deleted successfully!")
                return

        print("Student not found!")

    def save_students(self):
        data = []

        for student in self.students:
            data.append({
                "name": student.name,
                "student_id": student.student_id,
                "grade": student.grade
            })

        with open("students.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_students(self):
        try:
            with open("students.json", "r") as file:
                data = json.load(file)

            for student in data:
                new_student = Student(
                    student["name"],
                    student["student_id"],
                    student["grade"]
                )

                self.students.append(new_student)

        except FileNotFoundError:
            self.students = []

        except json.JSONDecodeError:
            print("Could not read students file.")
            self.students = []


manager = StudentManager()
manager.load_students()


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. List Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.list_students()

    elif choice == "3":
        manager.update_student()

    elif choice == "4":
        manager.delete_student()

    elif choice == "5":
        print("Student Management System is closing...")
        break

    else:
        print("Invalid choice!")
