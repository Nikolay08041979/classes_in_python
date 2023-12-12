class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)

    def rate_lector(self, lector, course, grade):  # для выставления оценок лекторам студентами
        if isinstance(lector, Lector) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
                print(f'Оценка {grade} по курсу {course} лектору {lector.name} {lector.surname} от студента {self.name} {self.surname} выставлена.')
                return
            else:
                lector.grades[course] = [grade]
                print(f'Оценка {grade} по курсу {course} лектору {lector.name} {lector.surname} от студента {self.name} {self.surname} выставлена.')
                return
        else:
            return 'Оценка лектору не выставлена'

    def get_average_student_rating_all_courses(self) -> float:  # для подсчета средней оценки за домашние задания по всем курсам, которые сдавал студент (в качестве аргументов принимаем список завершенных курсов и имя студента);
        if len(self.grades) == 0:
            return "У студента нет оценок"
        else:
            total = 0
            list_len_sum = 0
            for grade_list in self.grades.values():
                list_len_sum += len(grade_list)
                for grade in grade_list:
                    total += grade
            return round((total / list_len_sum), 1)

    def __str__(self):
        return (f'Имя: {self.name}\n' 
               f'Фамилия: {self.surname}\n' 
               f'Средняя оценка за домашние задания: {self.get_average_student_rating_all_courses()}\n' 
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)},\n' 
               f'Завершенные курсы: {", ".join(self.finished_courses)}\n')

    def __lt__(self, other_student):
        """Сравнение студентов"""
        if isinstance(other_student, Student) and len(self.grades) > 0 and len(other_student.grades) > 0:
            return (f'Средняя оценка студента {self.name} {self.surname} = {self.get_average_student_rating_all_courses()}\n'
                    f'Средняя оценка студента {other_student.name} {other_student.surname} = {other_student.get_average_student_rating_all_courses()}\n'
                    f'У студента {self.name} {self.surname} оценка выше.')
        else:
            return 'Нет оценки ни у одного из студентов.'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lector(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_lector_rating_all_courses(self) -> float:  # для подсчета средней оценки лектора за лекции по всем курсам, закрепленных за данным лектором (в качестве аргументов принимаем список курсов и имя лектора, за которым эти курсы закреплены)
        """Средняя оценка по курсам лектора"""
        if len(self.grades) == 0:
            return "Лектору не поставили оценок"
        else:
            total = 0
            list_len_sum = 0
            for grade_list in self.grades.values():
                list_len_sum += len(grade_list)
                for grade in grade_list:
                    total += grade
            return round((total / list_len_sum), 1)

    def __lt__(self, other_lector):
        """Сравнение лекторов"""
        if isinstance(other_lector, Lector) and len(self.grades) > 0 and len(other_lector.grades) > 0:
            return (f'Средняя оценка лектору {self.name} {self.surname} = {self.get_average_lector_rating_all_courses()}\n'
                    f'Средняя оценка лектору {other_lector.name} {other_lector.surname} = {other_lector.get_average_lector_rating_all_courses()}\n'
                    f'У лектора {self.name} {self.surname} оценка выше.')

    def __str__(self):
        """Вывод информации о лекторе"""
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.get_average_lector_rating_all_courses()}\n')

class Reviewer(Mentor):  # эксперты только могут проверять домашнее задание

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """Ревьювер ставит оценки студентам"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                print(f'Оценка {grade} у студента {student.name} {student.surname} за курс {course} от ревьювера {self.name} {self.surname} поставлена.\n')
                return
            else:
                student.grades[course] = [grade]
                print(f'Оценка {grade} у студента {student.name} {student.surname} за курс {course} от ревьювера {self.name} {self.surname} поставлена.\n')
                return
        else:
            return f'Ошибка. {self.name} не ревьюер'

    def __str__(self):
        """Вывод информации о ревьювере"""
        return(f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n')

if __name__ == '__main__':

    # Студенты

    nik_student = Student('Коля', 'Мазур', 'male')
    nik_student.add_courses_in_progress('Python')
    nik_student.add_finished_courses('Git')

    lera_student = Student('Лера', 'Мазур', 'female')
    lera_student.add_courses_in_progress('Git')
    lera_student.add_finished_courses('Python')

    students_list = [nik_student, lera_student]

    # Менторы

    bony_mentor = Mentor('Bony', 'Mono')
    clide_mentor = Mentor('Clide', 'Nano')
    bony_mentor.courses_attached.append('Git')
    clide_mentor.courses_attached.append('Python')
    mentors_list = [bony_mentor, clide_mentor]

    # Лекторы

    oleg_lector = Lector('Олег', 'Булыгин')
    oleg_lector.courses_attached.append('Python')
    alena_lector = Lector('Алёна', 'Батицкая')
    alena_lector.courses_attached.append('Git')
    lectors_list = [oleg_lector, alena_lector]

    nik_student.rate_lector(oleg_lector, 'Python', 10)
    lera_student.rate_lector(oleg_lector, 'Python', 9)
    lera_student.rate_lector(alena_lector, 'Git', 8)
    nik_student.rate_lector(alena_lector, 'Git', 7)

    # Ревьюеры

    monica = Reviewer('Monica', 'Beluchi')
    monica.courses_attached.append('Python')
    donald = Reviewer('Donald', 'Reygan')
    donald.courses_attached.append('Git')
    rev_list = [monica, donald]

    monica.rate_hw(nik_student, 'Python', 10)
    monica.rate_hw(lera_student, 'Git', 9)
    donald.rate_hw(nik_student, 'Python', 8)
    donald.rate_hw(lera_student, 'Git', 7)

    print('-------------------------------------------------------------------')
    print('Словарь с оценками студентов и лекторов:')  # Словарь с оценками студентов и лекторов
    print('-------------------------------------------------------------------')
    for student in students_list:
        print(f'Оценки {student.name}: {student.grades}')
    print()
    for lector in lectors_list:
        print(f'Оценки {lector.name}: {lector.grades}')
    print()

    def get_average_course_rating_all_students(some_list, course):
        """Средняя оценка студентов по курсу"""
        total_rate = []
        for person in some_list:
            if not isinstance(student, Student):
                return f'{person} не студент.'
            else:
                if course in person.grades:
                    total_rate += person.grades[course]
        res = round(sum(total_rate) / len(total_rate), 1)
        print(f'Средняя оценка студентов по курсу {course} = {res}')
        return

    def get_average_course_rating_all_lectors(some_list, course_name):
        """Средняя оценка лекторов по курсу"""
        total_rate = []
        for person in some_list:
            if not isinstance(person, Lector):
                return f'{person} не лектор.'
            else:
                if course_name in person.grades:
                    total_rate += person.grades[course_name]
        res = round(sum(total_rate) / len(total_rate), 1)
        print(f'Средняя оценка лекторов по курсу {course_name} = {res}')
        return


"""
Задача №3 Полиморфизм и магические методы 
"""

print(str(monica), str(donald), sep = '\n')
print(str(oleg_lector), str(alena_lector), sep = '\n')
print(str(nik_student), str(lera_student), sep = '\n')
print()
print('-------------------------------------------------------------------')
print('Рейтинги студентов и лекторов:')# Рейтинги студентов и лекторов
print('-------------------------------------------------------------------')
print(nik_student < lera_student)
print(oleg_lector < alena_lector)
print()

"""
Задача №4 Полевые испытания 
"""

get_average_course_rating_all_students(students_list, 'Python')
get_average_course_rating_all_students(students_list, 'Git')
get_average_course_rating_all_lectors(lectors_list, 'Git')
get_average_course_rating_all_lectors(lectors_list, 'Python')

