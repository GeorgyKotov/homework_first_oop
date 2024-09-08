class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finish_course(self, course_name: str):
        self.finished_courses.append(course_name)

    def add_course_in_progress(self, course_name: str):
        self.courses_in_progress.append(course_name)

    def make_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.finished_courses:
            if grade < 0 or grade > 10:
                return "Оценка вне диапазона возможных значений. Оценка может быть от 0 до 10"
            else:
                if course in lecturer.student_evaluation:
                    lecturer.student_evaluation[course] += [grade]
                else:
                    lecturer.student_evaluation[course] = [grade]
        else:
            return "Ошибка"

    def average_grade(self):
        if not self.grades:
            return 0
        all_grades = 0
        all_count = 0
        for grade in self.grades.values():
            all_grades += sum(grade)
            all_count += len(grade)
        return all_grades / all_count

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\n"
                f"Курсы в процессе изучения: {" ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}")

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_course_attached(self, course_name: str):
        self.courses_attached.append(course_name)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.student_evaluation = {}

    def average_grade(self):
        if not self.student_evaluation:
            return 0
        all_grades = 0
        all_count = 0
        for grade in self.student_evaluation.values():
            all_grades += sum(grade)
            all_count += len(grade)
        return all_grades / all_count

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


mike_vazovskiy = Student("Mike", "Vazovskiy", "Monster Male")
seliya_may = Student("Seliya", "May", "Monster Female")
randal_bogs = Mentor("Randal", "Bogs")
buu_sulivan = Mentor("Buu", "Sulivan")
jimbo_babangida = Lecturer("Jimbo", "Babangida")
donovan_mitchel = Lecturer("Donovan", "Mitchel")
mike_morales = Reviewer("Mike", "Morales")
rosa_roses = Reviewer("Rosa", "Roses")
mike_vazovskiy.add_course_in_progress("Scare")
mike_vazovskiy.add_finish_course("Hide")
seliya_may.add_course_in_progress("Hide")
seliya_may.add_finish_course("Scare")
donovan_mitchel.add_course_attached("Scare")
jimbo_babangida.add_course_attached("Hide")
rosa_roses.add_course_attached("Hide")
mike_morales.add_course_attached("Scare")
mike_morales.rate_hw(mike_vazovskiy, "Scare", 8)
rosa_roses.rate_hw(seliya_may, "Hide", 7)
mike_vazovskiy.make_grade(jimbo_babangida, "Hide", 10)
seliya_may.make_grade(donovan_mitchel, "Scare", 8)
mike_vazovskiy.average_grade()
seliya_may.average_grade()
jimbo_babangida.average_grade()
donovan_mitchel.average_grade()

print(seliya_may)
print()
print(mike_vazovskiy)
print()
print(mike_morales)
print()
print(rosa_roses)
print()
print(jimbo_babangida)
print()
print(donovan_mitchel)


def average_grade_for_all_students(list_students: list, name_course: str):
    average_score = 0
    average_score_student = 0
    if list_students:
        for student in list_students:
            if (name_course in student.courses_in_progress or name_course in student.finished_courses) and len(
                    student.grades[name_course]) > 0:
                average_score_student += sum(student.grades[name_course]) / len(student.grades[name_course])
                average_score += average_score_student
        return round(average_score / len(list_students), 2)


def average_grade_for_all_lectures(list_lectures: list, name_course: str):
    average_score = 0
    average_score_lecture = 0
    if list_lectures:
        for lecture in list_lectures:
            if name_course in lecture.courses_attached and len(lecture.student_evaluation[name_course]) > 0:
                average_score_lecture += sum(lecture.student_evaluation[name_course]) / len(
                    lecture.student_evaluation[name_course])
                average_score += average_score_lecture
        return round(average_score / len(list_lectures), 2)
