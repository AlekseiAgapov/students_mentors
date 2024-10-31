class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        sum_grades = 0
        count_grades = 0
        for course_grades in self.grades.values():
            sum_grades += sum(course_grades)
            count_grades += len(course_grades)
        return sum_grades / count_grades

    def __str__(self):
        average_grade = self.average_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {average_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() >= other.average_grade()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        sum_grades = 0
        count_grades = 0
        for course_grades in self.grades.values():
            sum_grades += sum(course_grades)
            count_grades += len(course_grades)
        return sum_grades / count_grades

    def __str__(self):
        average_grade = self.average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {average_grade:.1f}")
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() >= other.average_grade()

class Reviewer(Mentor):
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Creating students and mentors
# Students
student1 = Student('Валерий', 'Меладзе', 'male')
student1.courses_in_progress += ['Корейский язык', 'История Аргентины 19 века']
student1.finished_courses += ['Вокал', 'Оригами']

student2 = Student('Алла', 'Пугачева', 'female')
student2.courses_in_progress += ['Корейский язык', 'Git']
student2.finished_courses += ['Вокал', 'Python']

# Lecturers
lecturer1 = Lecturer('Сергей', 'Шнуров')
lecturer1.courses_attached += ['Корейский язык', 'История Аргентины 19 века']

lecturer2 = Lecturer('Алена', 'Апина')
lecturer2.courses_attached += ['Корейский язык', 'Git']

# Reviewers
reviewer1 = Reviewer('Филипп', 'Киркоров')
reviewer1.courses_attached += ['Корейский язык', 'История Аргентины 19 века']

reviewer2 = Reviewer('Анна', 'Асти')
reviewer2.courses_attached += ['Корейский язык', 'Git']

# Reviewers rate students' homework
reviewer1.rate_hw(student1, 'Корейский язык', 9)
reviewer1.rate_hw(student1, 'История Аргентины 19 века', 8)
reviewer1.rate_hw(student2, 'Корейский язык', 10)

reviewer2.rate_hw(student2, 'Корейский язык', 9)
reviewer2.rate_hw(student2, 'Git', 8)
reviewer2.rate_hw(student1, 'Корейский язык', 7)

# Applying the methods
# Students rate lecturers
student1.rate_lecturer(lecturer1, 'Корейский язык', 10)
student1.rate_lecturer(lecturer1, 'История Аргентины 19 века', 2)
student1.rate_lecturer(lecturer2, 'Корейский язык', 7)

student2.rate_lecturer(lecturer2, 'Корейский язык', 9)
student2.rate_lecturer(lecturer2, 'Git', 10)
student2.rate_lecturer(lecturer1, 'Корейский язык', 8)

# Printing information about students
print(student1)
print()
print(student2)
print()

# Printing information about lecturers
print(lecturer1)
print()
print(lecturer2)
print()

# Printing information about reviewers
print(reviewer1)
print()
print(reviewer2)
print()

# Let's compare the students
print(f"Студент {student1.name} {student1.surname} имеет более низкую среднюю оценку за домашние задания, чем студент {student2.name} {student2.surname}: {student1 < student2}")

# And the lecturers
print(f"Лектор {lecturer1.name} {lecturer1.surname} имеет такую же среднюю оценку за лекции, что и лектор {lecturer2.name} {lecturer2.surname}: {lecturer1 == lecturer2}")


# Part two: define the functions to calculate average scores for specific courses

def average_homework_score(student_list, course_name):
    """
    The function takes a list of students and a course name and returns average grade.
    If none of the students has any marks on that course, the function returns None.
    """
    sum_score = 0
    score_counter = 0
    for student in student_list:
        if course_name in student.grades:
            for score in student.grades[course_name]:
                score_counter += 1
                sum_score += score
    if sum_score == 0:
        return None
    else:
        return sum_score / score_counter

print(average_homework_score([student1, student2], 'Корейский язык'))


def average_lecturer_score(lector_list, course_name):
    """
    The function takes a list of lecturers and a course name and returns average grade.
    If none of the students has any marks on that course, the function returns None.
    """
    sum_score = 0
    score_counter = 0
    for lector in lector_list:
        if course_name in lector.grades:
            for score in lector.grades[course_name]:
                score_counter += 1
                sum_score += score
    if sum_score == 0:
        return None
    else:
        return sum_score / score_counter

print(average_lecturer_score([lecturer1, lecturer2], 'Корейский язык'))