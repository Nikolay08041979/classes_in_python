class Student:

    def __init__(self, name, surname, gender):
        self.student = None
        self.course = None
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.students_list = []
        self.students_rating = {}

    def rate_course(self, lector_name, course_name, grade):  # для выставления оценок лекторам студентами
        if not isinstance(lector_name,
                          Lector) or course_name not in self.finished_courses or course_name not in lector_name.courses_attached:
            return 'Ошибка'
        else:
            if course_name in lector_name.grades:
                lector_name.grades[course_name] += [grade]
            else:
                lector_name.grades[course_name] = [grade]

    def get_average_student_rating_one_course(self, student_name, course_name) -> float:  # для подсчета средней оценки за домашние задания по каждому законченному курсу данным студентом (в качестве аргументов принимаем имя студента и название курса, по которому он сдал дз);
        self.student = student_name
        self.course = course_name
        return round(sum(student_name.grades[course_name]) / len(student_name.grades[course_name]), 1)

    def get_average_student_rating_all_courses(self, student_name, course_name=None) -> float:  # для подсчета средней оценки за домашние задания по всем курсам, которые сдавал студент (в качестве аргументов принимаем список завершенных курсов и имя студента);
        total_ = 0
        self.student = student_name
        self.course = course_name
        for course_name in student_name.grades:
            total_ += self.get_average_student_rating_one_course(student_name, course_name)
        return round(total_ / len(student_name.grades), 1)

    def get_average_course_rating_all_students(self, course_name, student_name=None, students=None) -> float:  # для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
        total_ = 0
        self.course = course_name
        self.student = student_name
        self.students_list = students
        for student_name in students_list:
            for course_name in student_name.grades:
                total_ += self.get_average_student_rating_one_course(student_name, course_name)
        return round(total_ / len(students), 1)

    def __lt__(self, other):
        return self.get_average_student_rating_all_courses(self) < other.get_average_student_rating_all_courses(other)

    def __str__(self):
#        student_name: Student
        for student_name in students_list:
            return f'Имя: {self.name}\n' \
                   f'Фамилия: {self.surname}\n' \
                   f'Средняя оценка за домашние задания: {self.get_average_student_rating_all_courses(student_name)}\n' \
                   f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)},\n' \
                   f'Завершенные курсы: {", ".join(self.finished_courses)}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lector(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lector = None
        self.course = None
        self.courses_attached = []
        self.lectors_list = []
        self.grades = {}

    def get_average_lector_rating_one_course(self, lector_name, course_name) -> float:  # для подсчета средней оценки лектора за лекции по конректному курсу, закрепленному за данным лектором (в качестве аргументов принимаем наименование курса и имя лектора, за которым этот курс закреплен)
        self.name = lector_name
        self.course = course_name
        return round(sum(lector_name.grades[course_name]) / len(lector_name.grades[course_name]), 1)

    def get_average_lector_rating_all_courses(self, lector_name) -> float:  # для подсчета средней оценки лектора за лекции по всем курсам, закрепленных за данным лектором (в качестве аргументов принимаем список курсов и имя лектора, за которым эти курсы закреплены)
        total_ = 0
        self.name = lector_name
        for course_name in lector_name.grades:
            total_ += self.get_average_lector_rating_one_course(lector_name, course_name)
        return round(total_ / len(lector_name.grades), 1)

    def get_average_course_rating_all_lectors(self, lectors: list, course_name, lector_name=None) -> float:  # для подсчета средней оценки за лекции всех лекторов в рамках данному курса (в качестве аргумента принимаем список лекторов и название курса)
        total_ = 0
        self.course = course_name
        self.lectors_list = lectors
        self.lector = lector_name
        for lector_name in lectors:
            for course_name in lector_name.grades:
                total_ += self.get_average_lector_rating_one_course(lector_name, course_name)
        return round(total_ / len(lectors), 1)

    def __lt__(self, other):
        return self.get_average_lector_rating_all_courses(self) < other.get_average_lector_rating_all_courses(other)

    def __str__(self):
        for lector_name in lectors_list:
            return f'Имя: {self.name}\n' \
                   f'Фамилия: {self.surname}\n' \
                   f'Средняя оценка за лекции: {self.get_average_lector_rating_all_courses(lector_name)}\n'


class Reviewer(Mentor):  # эксперты только могут проверять домашнее задание

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.reviewers_list = []
        self.courses_attached = []

    def rate_hw(self, student_name, course_name, grade):
        if isinstance(student_name, Student) and (course_name in self.courses_attached or course_name in student_name.courses_in_progress):
            if course_name in student_name.grades:
                student_name.grades[course_name] += [grade]
            else:
                student_name.grades[course_name] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        for reviewer in reviewers_list:
            return f'Имя: {self.name}\n' \
                   f'Фамилия: {self.surname}\n'


# класс Student: Создание 2х экземпляров класса со всеми доступными атрибутами

student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_2 = Student('Your', 'Name', 'older_gender')

students_list = [student_1, student_2]

student_1.finished_courses = ['Python', 'Git', 'English', 'Java']
student_2.finished_courses = ['Java', 'Full Stack', 'Spanish', 'Python']

student_1.courses_in_progress = ['Spanish', 'Data Science', 'DevOps']
student_2.courses_in_progress = ['English', 'Git', 'Data Studio']

# Создание 2х экземпляров класса "Mentor" со всеми доступными атрибутами

mentor_1 = Mentor('Bony', 'Mono')
mentor_2 = Mentor('Clide', 'Nano')
mentor_1.courses_attached = ['Python', 'Full Stack', 'Git']
mentor_2.courses_attached = ['Java', 'English', 'Spanish']

# Создание 3х экземпляров класса "Lector" со всеми доступными атрибутами

lector_1 = Lector('Tommy', 'Cat')
lector_2 = Lector('Gerry', 'Mouse')
lector_3 = Lector('Scooby', 'Doo')

lectors_list = [lector_1, lector_2, lector_3]

lector_1.courses_attached = ['Python', 'Full Stack', 'Git', 'English']
lector_2.courses_attached = ['Java', 'Git', 'English', 'Spanish', 'DevOps']
lector_3.courses_attached = ['English', 'Spanish', 'Git', 'Java', 'DevOps']

student_1.rate_course(lector_1, 'Python', 10)
student_2.rate_course(lector_1, 'Python', 9)
student_2.rate_course(lector_1, 'Full Stack', 7)
student_1.rate_course(lector_2, 'Java', 7)
student_2.rate_course(lector_2, 'Java', 9)
student_1.rate_course(lector_2, 'Git', 8)
student_2.rate_course(lector_3, 'Spanish', 6)
student_1.rate_course(lector_3, 'English', 9)

# Создание 3х экземпляров класса "Reviewer" со всеми доступными атрибутами

reviewer_1 = Reviewer('Monica', 'Beluchi')
reviewer_2 = Reviewer('Donald', 'Reygan')
reviewer_3 = Reviewer('Snoop', 'Dogg')
reviewers_list = [reviewer_1, reviewer_2, reviewer_3]

reviewer_1.courses_attached = ['Python', 'Full Stack']
reviewer_2.courses_attached = ['Java', 'Git']
reviewer_3.courses_attached = ['English', 'Spanish']

## Оценки студентов за завершенные курсы

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Full Stack', 9)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Java', 9)
reviewer_1.rate_hw(student_1, 'Java', 6)
reviewer_3.rate_hw(student_1, 'English', 7)
reviewer_3.rate_hw(student_2, 'Spanish', 6)
reviewer_1.rate_hw(student_1, 'Python', 5)
reviewer_1.rate_hw(student_2, 'Full Stack', 3)
reviewer_1.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_1, 'Git', 4)
reviewer_2.rate_hw(student_2, 'Java', 5)
reviewer_1.rate_hw(student_1, 'Java', 7)
reviewer_3.rate_hw(student_1, 'English', 3)
reviewer_3.rate_hw(student_2, 'Spanish', 5)

## Оценки студентов за курсы в процессе обучения
reviewer_1.rate_hw(student_1, 'Data Science', 8)
reviewer_1.rate_hw(student_2, 'Data Studio', 9)
reviewer_2.rate_hw(student_1, 'Spanish', 10)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_3.rate_hw(student_1, 'DevOps', 7)
reviewer_3.rate_hw(student_2, 'English', 6)

print('-------------------------------------------------------------------')
print('Магические методы __repr__() и __str__():') # Магические методы __str__()
print('-------------------------------------------------------------------')
print(repr(reviewer_1),str(reviewer_1), sep = '\n')
print(repr(reviewer_2),str(reviewer_2), sep = '\n')
print(repr(reviewer_3),str(reviewer_3), sep = '\n')
print(repr(lector_1), str(lector_1), sep = '\n')
print(repr(lector_2), str(lector_2), sep = '\n')
print(repr(lector_3), str(lector_3), sep = '\n')
print(repr(student_1), str(student_1), sep = '\n')
print(repr(student_2), str(student_2), sep = '\n')
print()
print('-------------------------------------------------------------------')
print('Рейтинги студентов и лекторов:')# Рейтинги студентов и лекторов
print('-------------------------------------------------------------------')
print(f'Рейтинг студента #1 > студента #2: {student_2.__lt__(student_1)}')
print(f'Рейтинг лектора #1 > лектора #2: {lector_2.__lt__(lector_1)}')
print(f'Рейтинг лектора #2 > лектора #3: {lector_3.__lt__(lector_2)}')
print(f'Рейтинг лектора #1 > лектора #3: {lector_3.__lt__(lector_1)}')
print()

print('-------------------------------------------------------------------')
print('Словарь с оценками студентов и лекторов:') # Словарь с оценками студентов и лекторов
print('-------------------------------------------------------------------')
print(f'Оценки студента #1: {student_1.grades}')
print(f'Оценки студента #2: {student_2.grades}')
print()
print(f'Оценки лектора #1: {lector_1.grades}')
print(f'Оценки лектора #2: {lector_2.grades}')
print(f'Оценки лектора #3: {lector_3.grades}')
print()

"""
Задача №4 Полевые испытания 
"""
print('-------------------------------------------------------------------')
print('Средние оценки студентов') # Средение оценки студентов
print('-------------------------------------------------------------------')
print('Средние оценки ОДНОГО студента по ОДНОМУ курсу') ## Средние оценки конкретного студента по конкретному курсу
for course in student_1.grades:
    print(f'Ср оценка студента #1 за {course}: {student_1.get_average_student_rating_one_course(student_1, course)}')
print()
for course in student_2.grades:
    print(f'Ср оценка студента #2 за {course}: {student_2.get_average_student_rating_one_course(student_2, course)}')
print()
print('Средние оценки ОДНОГО студента по ВСЕМ курсам') ## Средние оценки конкретного студента по всем курсам
print(f'Ср оценка студента #1 по всем домашним заданиям / прошедшим курсам: {student_1.get_average_student_rating_all_courses(student_1)}')  # для подсчета средней оценки за домашние задания по всем курсам, которые сдавал студент (в качестве аргументов принимаем список завершенных курсов и имя студента);
print(f'Ср оценка студента #2 по всем домашним заданиям / прошедшим курсам: {student_2.get_average_student_rating_all_courses(student_2)}')
print()
print('Средние оценки ВСЕХ студентов по ОДНОМУ курсу') ## Средение оценки всех студентов за конкрентный курс
for course in student_1.grades:
    print(f'Ср оценка всех студентов по {course}: {student_1.get_average_student_rating_all_courses(student_1,course)}')
for course in student_2.grades:
    print(f'Ср оценка всех студентов по {course}: {student_2.get_average_student_rating_all_courses(student_2,course)}')
print()
print('-------------------------------------------------------------------')
print('Средние оценки лекторов') # Средение оценки лекторов
print('-------------------------------------------------------------------')
print('Средняя оценка ОДНОГО лектора по ОДНОМУ курсу') ## Средняя оценка конкретного лектора по заданному курсу
for course in lector_1.grades:
    print(f'Ср оценка лектора #1 за {course}: {lector_1.get_average_lector_rating_one_course(lector_1, course)}')
for course in lector_2.grades:
    print(f'Ср оценка лектора #2 за {course}: {lector_2.get_average_lector_rating_one_course(lector_2, course)}')
for course in lector_3.grades:
    print(f'Ср оценка лектора #2 за {course}: {lector_3.get_average_lector_rating_one_course(lector_3, course)}')
print()
print('Средняя оценка ОДНОГО лектора по ВСЕМ закрепленным курсам') ## Средняя оценка конкретного лектора по всем курсам
print(f'Ср оценка лектора #1 по всем закрепленным курсам: {lector_1.get_average_lector_rating_all_courses(lector_1)}')
print(f'Ср оценка лектора #2 по всем закрепленным курсам: {lector_2.get_average_lector_rating_all_courses(lector_2)}')
print(f'Ср оценка лектора #3 по всем закрепленным курсам: {lector_3.get_average_lector_rating_all_courses(lector_3)}')
print()
print('Средняя оценка ВСЕХ лекторов по ОДНОМУ курсу') ## Средняя оценка всех лекторов по конкретному курсу
for course in lector_1.grades:
    print(f'Ср оценка лекторов по {course}: {lector_1.get_average_course_rating_all_lectors(lectors_list, course)}')
for course in lector_2.grades:
    print(f'Ср оценка лекторов по {course}: {lector_2.get_average_course_rating_all_lectors(lectors_list, course)}')
for course in lector_3.grades:
    print(f'Ср оценка лекторов по {course}: {lector_3.get_average_course_rating_all_lectors(lectors_list, course)}')
print()
print()


