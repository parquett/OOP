import json
from enum import Enum
from datetime import date


class StudyField(Enum):
    MECHANICAL_ENGINEERING = 1
    SOFTWARE_ENGINEERING = 2
    FOOD_TECHNOLOGY = 3
    URBANISM_ARCHITECTURE = 4
    VETERINARY_MEDICINE = 5


class Student:
    def __init__(self, firstname, lastname, email, enrollment_date, date_of_birth):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.enrollment_date = enrollment_date
        self.date_of_birth = date_of_birth
        self.faculty = None
        self.graduate = False

    def graduate_student(self):
        self.graduate = True

    def assign_to_faculty(self, faculty):
        self.faculty = faculty

    def to_dict(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "enrollment_date": str(self.enrollment_date),
            "date_of_birth": str(self.date_of_birth),
            "faculty": self.faculty.name if self.faculty else None,
            "graduate": self.graduate,
        }

    @classmethod
    def from_dict(cls, data):
        #enrollment_date = date.fromisoformat(data["enrollment_date"])
        #date_of_birth = date.fromisoformat(data["date_of_birth"])
        student = cls(
            data["firstname"],
            data["lastname"],
            data["email"],
            data["enrollment_date"],
            data["date_of_birth"],
        )
        student.graduate = data["graduate"]
        return student


class Faculty:
    def __init__(self, name, abbreviation, studyfield):
        self.name = name
        self.abbreviation = abbreviation
        self.studyfield = studyfield
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def to_dict(self):
        return {
            "name": self.name,
            "abbreviation": self.abbreviation,
            "studyfield": self.studyfield.name,
            "students": [student.email for student in self.students],
        }

    @classmethod
    def from_dict(cls, data):
        studyfield = StudyField[data["studyfield"]]
        faculty = cls(data["name"], data["abbreviation"], studyfield)
        faculty.students = data["students"]
        return faculty


class University:
    def __init__(self):
        self.students = []
        self.faculties = []

    def create_student(self):
        firstname = input("Enter student's first name: ")
        lastname = input("Enter student's last name: ")
        email = input("Enter student's email: ")
        enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
        date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")

        enrollment_date = date.fromisoformat(enrollment_date)
        date_of_birth = date.fromisoformat(date_of_birth)

        student = Student(firstname, lastname, email, enrollment_date, date_of_birth)
        self.students.append(student)
        return student

    def create_faculty(self):
        name = input("Enter faculty name: ")
        abbreviation = input("Enter faculty abbreviation: ")
        print("Select study field:")
        for field in StudyField:
            print(f"{field.value}. {field.name.replace('_', ' ')}")
        studyfield = StudyField(int(input("Enter the number of the study field: ")))

        faculty = Faculty(name, abbreviation, studyfield)
        self.faculties.append(faculty)
        return faculty

    def assign_student_to_faculty(self):
        email = input("Enter student's email: ")
        faculty_name = input("Enter faculty name: ")

        student = next((s for s in self.students if s.email == email), None)
        faculty = next((f for f in self.faculties if f.name == faculty_name), None)

        if student and faculty:
            student.assign_to_faculty(faculty)
            faculty.add_student(student)
            print(f"{student.firstname} {student.lastname} has been assigned to {faculty.name}.")
        else:
            print("Student or faculty not found.")

    def display_current_students(self):
        for faculty in self.faculties:
            print(f"Faculty: {faculty.name}")
            for student in faculty.students:
                print(f" - {student.firstname} {student.lastname}")

    def graduate(self):
        em = input("Enter student's email: ")
        for student in self.students:
            if student.email == em:
                student.graduate = True
        print("Student has been graduated.")

    def display_graduates(self):
        print("Graduated Students:")
        for student in self.students:
            if student.graduate:
                print(f"{student.firstname} {student.lastname}")

    def check_student_belongs_to_faculty(self):
        stud_email = input("Enter student's email: ")
        faculty_name = input("Enter faculty name: ")

        student = next((s for s in self.students if s.email == stud_email), None)
        if student and student.faculty and student.faculty.name == faculty_name:
            print(f"Yes, this student belongs to this faculty.")
        else:
            print(f"No student with this email found in this faculty.")

    def search_faculty_by_student_identifier(self):
        identifier = input("Enter student's email: ")
        student = next((s for s in self.students if s.email == identifier), None)

        if student:
            if student.faculty:
                print(f"{student.firstname} {student.lastname} belongs to {student.faculty.name} faculty.")
            else:
                print(f"{student.firstname} {student.lastname} is not assigned to any faculty.")
        else:
            print("Student not found.")

    def display_university_faculties(self):
        print("University Faculties:")
        for faculty in self.faculties:
            print(f" - {faculty.name} ({faculty.abbreviation})")

    def display_faculties_by_field(self):
        print("Select study field:")
        for field in StudyField:
            print(f"{field.value}. {field.name.replace('_', ' ')}")
        studyfield = StudyField(int(input("Enter the corresponding number: ")))

        print(f"Faculties in the {studyfield.name.replace('_', ' ')} field:")
        for faculty in self.faculties:
            if faculty.studyfield == studyfield:
                print(f" - {faculty.name} ({faculty.abbreviation})")

    def save_data(self):
       try:
           with open("university_data.json", "w") as file:
            data = {
                "students": [student.to_dict() for student in self.students],
                "faculties": [faculty.to_dict() for faculty in self.faculties],
            }
            json.dump(data, file, indent=4)
       except Exception as e:
           print("Error", e)

    def load_data(self):
        try:
            with open("university_data.json", "r") as file:
                data = json.load(file)
                self.students = [Student.from_dict(student_data) for student_data in data["students"]]
                self.faculties = [Faculty.from_dict(faculty_data) for faculty_data in data["faculties"]]

                for faculty in self.faculties:
                    faculty.students = [student for student in self.students if student.faculty == faculty.name]
                    for student in faculty.students:
                        student.faculty = faculty.name
                #print("!!!!!!!",faculty.students,"!!!!!!!!") #for debug
        except FileNotFoundError:
            pass


def main():
    university = University()
    university.load_data()  # Load data from previous runs

    while True:
        print("\n1 - Faculty operations")
        print("2 - General operations")
        print("0 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nFaculty operations")
            print("1. Create and assign a student to a faculty.")
            print("2. Graduate a student from a faculty.")
            print("3. Display current enrolled students.")
            print("4. Display graduates.")
            print("5. Check if a student belongs to a faculty.")
            print("0. Exit.")

            choice1 = input("Enter your choice: ")

            if choice1 == "1":
                student = university.create_student()
                university.assign_student_to_faculty()
            elif choice1 == "2":
                university.graduate()
            elif choice1 == "3":
                university.display_current_students()
            elif choice1 == "4":
                university.display_graduates()
            elif choice1 == "5":
                university.check_student_belongs_to_faculty()
            elif choice1 == "0":
                continue
            else:
                print("No such option, please try again.")
        elif choice == "2":
            print("\nGeneral Operations:")
            print("1. Create a new faculty.")
            print("2. Search what faculty a student belongs to.")
            print("3. Display University faculties.")
            print("4. Display all faculties belonging to a field.")
            print("0. Exit")

            choice1 = input("Enter your choice: ")

            if choice1 == "1":
                university.create_faculty()
            elif choice1 == "2":
                university.search_faculty_by_student_identifier()
            elif choice1 == "3":
                university.display_university_faculties()
            elif choice1 == "4":
                university.display_faculties_by_field()
            elif choice1 == "0":
                continue
            else:
                print("No such option, please try again.")
        elif choice == "0":
            university.save_data()
            break
        else:
            print("No such option, please try again.")



if __name__ == "__main__":
    main()
