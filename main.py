
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self._id = None

    def get_id(self):
        return self._id

    def display_detail(self):
        return f"Name: {self.name}, Email: {self.email}, ID: {self._id}"

class Student(Person):
    _id_Counter = 100

    def __init__(self, name, email,grade):
        super().__init__(name, email)

        Student._id_Counter += 1
        self._id = f"STU{Student._id_Counter}"

        self.grade = grade
        self.enrolled_courses = []

    def enroll_course(self, course_id):
        if course_id not in self.enrolled_courses:
            self.enrolled_courses.append(course_id)

    def display_details(self):
        return (
            f"Student ID: {self._id} | "
            f"Name: {self.name} | "
            f"Email: {self.email} | "
            f"Grade: {self.grade}"
         )
class Trainer(Person):
    _id_Counter = 500

    def __init__(self, name, email, specialization):
        super().__init__(name, email)

        Trainer._id_Counter += 1
        self._id = f"TRN{Trainer._id_Counter}"

        self.specialization = specialization

    def assign_course(self, course_name):
        print(f"{course_name} Assigned To {self.name}")

    def display_details(self):
        return (
            f"Trainer ID: {self._id} | "
            f"Name: {self.name} | "
            f"Specialization: {self.specialization}"
            )
class Course:
    _id_Counter = 800

    def __init__(self,course_name,duration,trainer):
        Course._id_Counter += 1

        self.course_id = f"CRS{Course._id_Counter}"
        self.course_name = course_name
        self.duration = duration
        self.trainer = trainer

    def display_details(self):
        return (
        f"Course ID: {self.course_id} | "
        f"Course Name: {self.course_name} | "
        f"Duration: {self.duration} | "
        f"Trainer: {self.trainer.name}"
        )
class Enrollment:
    def __init__(self,student,course):
        self.student = student
        self.course = course

        self.__progress = 0

    def update_progress(self,progress):
        if 0 <= progress <= 100:
            self.__progress = progress

        else:
            print("Invalid Progress")

    def get_progress(self):
        return self.__progress


    def display_details(self):
        return (
            f"{self.student.name} -> "
            f"{self.course.course_name} | "
            f"Progress: {self.__progress}%"
        )

class Tokenizer:


    def tokenize(self, text):
        return text.split()

    def token_count(self, text):
        return len(self.tokenize(text))

    def word_frequency(self, text):

        frequency = {}

        for word in self.tokenize(text):

            if word in frequency:
                    frequency[word] += 1
            else:
                    frequency[word] = 1

        return frequency
class SLMSSystem:

    def __init__(self):

        self.students = {}
        self.trainers = {}
        self.courses = {}
        self.enrollments = []
#Add Student Method
    def add_student(self,name,email,grade):
        student = Student(name,email,grade)
        self.students[student.get_id()] = student
        print(f"Student Added Successfully. ID: {student.get_id()}")

#Add Trainer Method
    def add_trainer(self, name,email,specialization):
        trainer = Trainer(
            name,
            email,
            specialization
        )
        self.trainers[trainer.get_id()] = trainer

        print(f"Trainer Added Successfully. ID: {trainer.get_id()}")
#Creating Course File
    def create_course(
            self,
            course_name,
            duration,
            trainer_id
            ):
        if trainer_id not in self.trainers:
            print("Trainer Not Found")
            return

        trainer = self.trainers[trainer_id]

        course = Course(
            course_name,
            duration,
            trainer
            )

        self.courses[course.course_id] = course
        trainer.assign_course(course.course_name)
        print(f"Course Created Successfully. ID: {course.course_id}")
#Enroll Studdent Method
    def enroll_student(self,student_id,course_id):
        if student_id not in self.students:
            print("Student Not Found")
            return

        if course_id not in self.courses:
            print("Course Is Not Found")
            return

        student = self.students[student_id]
        course = self.courses[course_id]

        if course_id in student.enrolled_courses:
            print("Student Already Enrolled")
            return

        student.enroll_course(course_id)

        enrollment = Enrollment(
            student,
            course
            )

        self.enrollments.append(enrollment)
        print("Enrollment Successfully")
#Update Progress Method
    def update_progress(self, student_id, course_id, progress):

        for enrollment in self.enrollments:

            if (
                enrollment.student.get_id() == student_id
                and
                enrollment.course.course_id == course_id
                ):
                enrollment.update_progress(progress)

                print("Progress Updated")

                return

            print("Enrollment Not Found")
#Search Students Methods
    def search_student(self, student_id):

        if student_id not in self.students:
            print("Student Not Found")
            return

        student = self.students[student_id]

        print(student.display_details())

        for enrollment in self.enrollments:

            if enrollment.student.get_id() == student_id:
                print(enrollment.display_details())
#Main Saving File
    # student saving file
    def save_data(self):
        with open("students.txt", "w") as file:
            for student in self.students.values():
                file.write(
                    f"{student.get_id()},"
                    f"{student.name},"
                    f"{student.email},"
                    f"{student.grade}\n"
                    )



#Trainer saving file
        with open("trainers.txt", "w") as file:

                for trainer in self.trainers.values():
                    file.write(
                        f"{trainer.get_id()},"
                        f"{trainer.name},"
                        f"{trainer.email},"
                        f"{trainer.specialization}\n"
                    )
#Courses Saving file
        with open ("Courses.txt","w") as file:
            for course in self.courses.values():
                file.write(
                f"{course.course_id},"
                f"{course.course_name},"
                f"{course.duration},"
                f"{course.trainer.get_id()}\n"
                )



#Enrollment Saving file
        with open("enrollments.txt", "w") as file:

                for enrollment in self.enrollments:
                    file.write(
                        f"{enrollment.student.get_id()},"
                        f"{enrollment.course.course_id},"
                        f"{enrollment.get_progress()}\n"
                        )

                print("\nAll Data Saved Successfully")
#load Student File
    def load_students(self):
        try:
            highest_id = 100
            with open("students.txt","r") as file:
                for line in file:
                    student_id,name,email,grade = line.strip().split(",")
                    student = Student(
                    name,
                    email,
                    grade
                    )

                    student._id = student_id
                    self.students[student_id] = student
                    num = int(student_id.replace("STU",""))
                    if num > highest_id:
                        highest_id = num
                Student._id_Counter = highest_id
        except FileNotFoundError:
            print("No Student File Found")
#load trainers file
    def load_trainers(self):
        try:
            highest_id = 500
            with open("trainers.txt","r") as file:
                for line in file:
                    trainer_id,name,email,specialization = line.strip().split(",")

                    trainer = Trainer(
                    name,
                    email,
                    specialization
                    )

                    trainer._id = trainer_id
                    self.trainers[trainer_id] = trainer
                    num = int(trainer_id.replace("TRN",""))
                    if num > highest_id:
                        highest_id = num
                    Trainer._id_Counter = highest_id
        except FileNotFoundError:
            print("No Trainer File Found")
#load Courses File
    def load_courses(self):
        try:
            highest_id = 800
            with open("courses.txt","r") as file:
                for line in file:
                    course_id,course_name,duration,trainer_id = line.strip().split(",")
                    trainer = self.trainers[trainer_id]
                    course = Course(
                    course_name,
                    duration,
                    trainer
                    )
                    course._id = course_id
                    self.courses[course_id] = course
                    num = int(course_id.replace("CRS",""))
                    if num > highest_id:
                        highest_id = num
                    Course._id_Counter = highest_id
        except FileNotFoundError:
                print("No Course File Found")

#load Enrollment
    def load_enrollment(self):
        try:
            with open("enrollments.txt", "r") as file:
                for line in file:
                    student_id, course_id, progress = line.strip().split(",")

                    student = self.students[student_id]
                    course = self.courses[course_id]

                    # ADD THIS LINE
                    student.enroll_course(course_id)

                    enrollment = Enrollment(
                        student,
                        course
                    )

                    enrollment.update_progress(
                        int(progress)
                    )

                    self.enrollments.append(
                        enrollment
                    )

        except FileNotFoundError:
            print("No Enrollment File Found")
#Delete Student
    def delete_student(self, student_id):

        if student_id not in self.students:
            print("Student Not Found")
            return

        del self.students[student_id]

        print("Student Deleted Successfully")
#Delete Trainer
    def delete_trainer(self, trainer_id):

        if trainer_id not in self.trainers:
            print("Trainer Not Found")
            return

        for course in self.courses.values():

            if course.trainer.get_id() == trainer_id:

                print(
                    f"Trainer Is Assigned To Course: "
                    f"{course.course_name}"
                )

            choice = input(
                "Are You Sure You Want To Delete This Trainer? (Y/N): "
            ).upper()

            if choice != "Y":
                print("Deletion Cancelled")
                return

            break

        del self.trainers[trainer_id]

        print("Trainer Deleted Successfully")
#Delete Cousres
    def delete_course(self, course_id):

        if course_id not in self.courses:
            print("Course Not Found")
            return

        del self.courses[course_id]
        print("Course Deleted Successfully")

#Search Knowledge Base")
    def search_knowledge_base(self, keyword):

        try:
            with open("knowledge_base.txt", "r") as file:
                content = file.read()

            topics = content.split("TOPIC:")

            found = False

            for topic in topics:

                lines = topic.strip().split("\n")

                if not lines:
                    continue

                topic_name = lines[0].strip()

                if keyword.lower() == topic_name.lower():
                    print("\nTOPIC:")
                    print(topic)

                    found = True
                    break

            if not found:
                print("No Information Found")

        except FileNotFoundError:
            print("Knowledge Base File Not Found")


def main():
    system = SLMSSystem()
    system.load_students()
    system.load_trainers()
    system.load_courses()
    system.load_enrollment()
    print("\nData Loaded Successfully")

    while True:
        print("\n===== LMS MENU =====")
        print("1. Add Student")
        print("2. Add Trainer")
        print("3. Create Course")
        print("4. Enroll Student")
        print("5. Update Progress")
        print("6. View Students")
        print("7. View Courses")
        print("8. View Trainers")
        print("9. Search Student")
        print("10. Save Data")
        print("11. Delete Student")
        print("12. Delete Trainer")
        print("13. Delete Course")
        print("14. Slms Ai")
        print("15. Tokenization Engine")
        print("16. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            student_name = input("Enter Student Name: ")
            student_email = input("Enter Student Email: ")
            grade = input("Enter Grade: ")
            system.add_student(student_name,
                               student_email,
                               grade
                               )


        elif choice == "2":
            trainer_name = input("Enter Trainer Name: ")
            trainer_email = input("Enter Trainer Email: ")
            trainer_specialization = input("Enter Trainer Specialization: ")
            system.add_trainer(trainer_name,
                               trainer_email,
                               trainer_specialization)


        elif choice == "3":

            if not system.trainers:
                print("No Trainers Available")
                continue

            course_name = input("Enter Course Name: ")
            duration = input("Enter Course Duration: ")

            know_id = input(
                "Do You Know The Trainer ID? (yes/no): "
            ).lower()

            if know_id == "no":

                print("\n====== AVAILABLE TRAINERS ======")

                for trainer in system.trainers.values():
                    print(trainer.display_details())

            trainer_id = input(
                "\nEnter Trainer ID: "
            ).upper()

            system.create_course(
                course_name,
                duration,
                trainer_id
            )


        elif choice == "4":
            student_id = input("Enter Student ID: ").upper()
            course_id = input("Enter Course ID: ").upper()
            system.enroll_student(student_id,
                                  course_id)


        elif choice == "5":
            student_id = input("Enter Student ID: ").upper()
            course_id = input("Enter Course ID: ").upper()
            progress = int(input("Enter Progress(0 TO 100): "))
            system.update_progress(
                student_id,
                course_id,
                progress
             )


        elif choice == "6":

            print("\n==================== STUDENTS ====================")

            print(
                f"{'STUDENT ID':<12}"
                f"{'NAME':<20}"
                f"{'EMAIL':<30}"
                f"{'GRADE':<8}"
                f"{'PROGRESS':<12}"
                f"{'ENROLLED COURSE NAME AND ID'}"

            )

            print("-" * 120)

            for student in system.students.values():

                enrolled_course_names = []
                progress_list = []

                for enrollment in system.enrollments:

                    if enrollment.student.get_id() == student.get_id():
                        enrolled_course_names.append(
                            f"{enrollment.course.course_id}-{enrollment.course.course_name}"
                        )

                        progress_list.append(
                            enrollment.get_progress()
                        )

                courses = ", ".join(enrolled_course_names)

                if not courses:
                    courses = "Not Enrolled"

                if progress_list:
                    avg_progress = sum(progress_list) / len(progress_list)
                    progress_text = f"{avg_progress:.0f}%"
                else:
                    progress_text = "0%"

                print(
                    f"{student.get_id():<12}"
                    f"{student.name:<20}"
                    f"{student.email:<30}"
                    f"{student.grade:<8}"
                    f"{progress_text:<12}"
                    f"{courses}"

                )


        elif choice == "7":
            print("\n{:<10} {:<30} {:<15} {:<20} {:<8}".format(
                "COURSE_ID","COURSE_NAME","DURATION","TRAINER_NAME", "TRAINER_ID"
            ))

            print("-" * 90)

            for course in system.courses.values():
                print("{:<10} {:<30} {:<15} {:<20} {:8}".format(
                    course.course_id,
                    course.course_name,
                    course.duration,
                    course.trainer.name,
                    course.trainer.get_id()
                ))



        elif choice == "8":
            print("\n{:<10} {:<20} {:<40} {:<25}".format(
                "ID",
                "NAME",
                "EMAIL",
                "SPECIALIZATION"
            ))

            print("-" * 100)

            for trainer in system.trainers.values():
                print("{:<10} {:<20} {:<40} {:<25}".format(
                    trainer.get_id(),
                    trainer.name,
                    trainer.email,
                    trainer.specialization
                ))


        elif choice == "9":

            student_id = input("Enter Student ID: ").upper()
            system.search_student(student_id)


        elif choice == "10":
            system.save_data()

        elif choice =="11":
            student_id = input("Enter Student Id: ").upper()
            system.delete_student(student_id)

        elif choice == "12":
            trainer_id = input("Enter Trainer ID: ").upper()
            system.delete_trainer(trainer_id)

        elif choice == "13":
            course_id = input("Enter Course ID: ").upper()
            system.delete_course(course_id)

        elif choice == "14":
            keyword = input("How Can I Help You: ")
            system.search_knowledge_base(keyword)

        elif choice == "15":


            text = input("Enter Text: ")

            tokenizer = Tokenizer()

            print("\nTokens:")
            print(tokenizer.tokenize(text))

            print(
                f"\nToken Count: "
                f"{tokenizer.token_count(text)}"
            )

            print("\nWord Frequency:")

            frequency = tokenizer.word_frequency(text)

            for word, count in frequency.items():
                print(
                    f"{word} : {count}"
                )

        elif choice == "16":
            print("Thank You For Using LMS")
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()


