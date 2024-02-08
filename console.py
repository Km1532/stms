# -*- coding: utf-8 -*-

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_schedule_project.settings')
application = get_wsgi_application()
from school_schedule_app.models import Subject, Teacher, Class, Student, Lesson

class SchoolSchedule:
    def display_subjects(self):
        subjects = Subject.objects.all()
        print("Предмети:")
        for subject in subjects:
            print(f"- {subject.name}")

    def display_teachers(self):
        teachers = Teacher.objects.all()
        print("\nВчителі:")
        for teacher in teachers:
            print(f"- {teacher.name} ({teacher.subject.name})")

    def display_classes(self):
        classes = Class.objects.all()
        print("\nКласи:")
        for class_obj in classes:
            print(f"- {class_obj.name}")

    def display_students(self):
        students = Student.objects.all()
        print("\nУчні:")
        for student in students:
            print(f"- {student.name} (клас {student.class_name.name})")

    def display_student_schedule(self, student_name):
        try:
            student = Student.objects.get(name=student_name)
            lessons = Lesson.objects.filter(student=student)
            print(f"\nРозклад уроків для учня {student_name} (клас {student.class_name.name}):")
            for lesson in lessons:
                print(f"- {lesson.subject.name} ({lesson.day}, {lesson.time}, вчитель: {lesson.teacher.name})")
        except Student.DoesNotExist:
            print(f"Учень {student_name} не знайдений.")

    def add_student_schedule(self, student_name):
        try:
            student = Student.objects.get(name=student_name)
            self.display_student_schedule(student_name)
            subject_name = input("Введіть назву предмету: ")
            day = input("Введіть день (наприклад, Понеділок): ")
            time = input("Введіть час (наприклад, 10:00): ")

            self._add_student_schedule_to_database(student, subject_name, day, time)
        except Student.DoesNotExist:
            print(f"Учень {student_name} не знайдений.")

    def _add_student_schedule_to_database(self, student, subject_name, day, time):
        try:
            subjects = Subject.objects.filter(name=subject_name)
            if subjects.exists():
                subject = subjects.first()
                teacher_name = input("Введіть ім'я вчителя: ")
                teacher = Teacher.objects.get(name=teacher_name)
                lesson = Lesson(teacher=teacher, subject=subject, class_obj=student.class_name, day=day, time=time, student=student)
                lesson.save()
                print("Розклад уроку додано успішно.")
            else:
                print(f"Предмет {subject_name} не знайдений.")
        except Teacher.DoesNotExist:
            print(f"Вчитель {teacher_name} не знайдений.")

    def add_subject(self, name):
        subject = Subject(name=name)
        subject.save()
        print(f"Предмет {name} додано успішно.")

    def add_teacher(self, name, subject_name):
        try:
            subject = Subject.objects.get(name=subject_name)
            teacher = Teacher(name=name, subject=subject)
            teacher.save()
            print(f"Вчитель {name} додано успішно.")
        except Subject.DoesNotExist:
            print(f"Предмет {subject_name} не знайдений.")

    def add_class(self, name):
        class_obj = Class(name=name)
        class_obj.save()
        print(f"Клас {name} додано успішно.")

    def add_student(self, name, class_name):
        try:
            class_obj = Class.objects.get(name=class_name)
            student = Student(name=name, class_name=class_obj)
            student.save()
            print(f"Учня {name} додано успішно.")
        except Class.DoesNotExist:
            print(f"Клас {class_name} не знайдений.")

    def display_teacher_schedule(self, teacher_name):
        try:
            teacher = Teacher.objects.get(name=teacher_name)
            lessons = Lesson.objects.filter(teacher=teacher)
            print(f"\nРозклад уроків для вчителя {teacher_name}:")
            for lesson in lessons:
                print(f"- {lesson}")
        except Teacher.DoesNotExist:
            print(f"Вчитель {teacher_name} не знайдений.")

    def add_teacher_schedule(self, teacher_name):
        try:
            teacher = Teacher.objects.get(name=teacher_name)
            self.display_teacher_schedule(teacher_name)
            subject_name = input("Введіть назву предмету: ")
            day = input("Введіть день (наприклад, Понеділок): ")
            time = input("Введіть час (наприклад, 10:00): ")

            try:
                subject = Subject.objects.get(name=subject_name)
                class_name = input("Введіть назву класу: ")
                class_obj = Class.objects.get(name=class_name)
                lesson = Lesson(teacher=teacher, subject=subject, class_obj=class_obj, day=day, time=time)
                lesson.save()
                print("Розклад уроку додано успішно.")
            except Subject.DoesNotExist:
                print(f"Предмет {subject_name} не знайдений.")
            except Class.DoesNotExist:
                print(f"Клас {class_name} не знайдений.")
        except Teacher.DoesNotExist:
            print(f"Вчитель {teacher_name} не знайдений.")

    def daily_journal_menu(self):
        while True:
            print("\nМеню Щоденника:")
            print("1. Вчителі")
            print("2. Учні")
            print("3. Назад")

            choice = input("Введіть свій вибір (1-3): ")

            if choice == "1":
                self.teachers_journal_menu()
            elif choice == "2":
                self.students_journal_menu()
            elif choice == "3":
                break
            else:
                print("Невірний вибір. Будь ласка, введіть число від 1 до 3.")

    def teachers_journal_menu(self):
        teacher_name = input("Введіть ім'я вчителя: ")
        subject_name = input("Введіть назву предмету: ")

        try:
            teacher = Teacher.objects.get(name=teacher_name)
            subject = Subject.objects.get(name=subject_name)

            students = Student.objects.filter(class_name__teacher=teacher, class_name__subject=subject)

            for student in students:
                grade = input(f"Введіть оцінку для учня {student.name} (1-12): ")

                try:
                    lesson = Lesson.objects.get(teacher=teacher, subject=subject, class_obj=student.class_name)
                    lesson.grade = int(grade)
                    lesson.save()
                    print(f"Оцінка для учня {student.name} успішно збережена.")
                except Lesson.DoesNotExist:
                    print(f"Розклад уроків для учня {student.name} не знайдений.")
        except Teacher.DoesNotExist:
            print(f"Вчитель {teacher_name} не знайдений.")
        except Subject.DoesNotExist:
            print(f"Предмет {subject_name} не знайдений.")

    def students_journal_menu(self):
        student_name = input("Введіть ім'я учня: ")

        try:
            student = Student.objects.get(name=student_name)
            lessons = Lesson.objects.filter(student=student)

            print(f"\nОцінки для учня {student_name} (клас {student.class_name.name}):")
            for lesson in lessons:
                print(f"{lesson.subject.name}: {lesson.grade if lesson.grade is not None else 'Оцінка не виставлена'}")
        except Student.DoesNotExist:
            print(f"Учень {student_name} не знайдений.")

    def display_main_menu(self):
        print("\nГоловне меню:")
        menu_options = [
            "Відображення Предметів",
            "Відображення Вчителів",
            "Відображення Класів",
            "Відображення Учнів",
            "Додати предмет",
            "Додати вчителя",
            "Додати клас",
            "Додати учня",
            "Переглянути розклад для вчителя",
            "Додати розклад для вчителя",
            "Переглянути розклад для учня",
            "Додати розклад для учня",
            "Щоденник",
            "Про нас",
            "Про Школу/Ліцей",
            "Вихід"
        ]
        for i, option in enumerate(menu_options, start=1):
            print(f"{i}. {option}")

    def main_menu(self):
        while True:
            self.display_main_menu()
            choice = input("Введіть свій вибір (1-16): ")

            if choice == "1":
                self.display_subjects()
            elif choice == "2":
                self.display_teachers()
            elif choice == "3":
                self.display_classes()
            elif choice == "4":
                self.display_students()
            elif choice == "5":
                name = input("Введіть назву предмету: ")
                self.add_subject(name)
            elif choice == "6":
                name = input("Введіть ім'я вчителя: ")
                subject_name = input("Введіть назву предмету, який викладає вчитель: ")
                self.add_teacher(name, subject_name)
            elif choice == "7":
                name = input("Введіть назву класу: ")
                self.add_class(name)
            elif choice == "8":
                name = input("Введіть ім'я учня: ")
                class_name = input("Введіть назву класу, до якого належить учень: ")
                self.add_student(name, class_name)
            elif choice == "9":
                teacher_name = input("Введіть ім'я вчителя: ")
                self.display_teacher_schedule(teacher_name)
            elif choice == "10":
                teacher_name = input("Введіть ім'я вчителя: ")
                self.add_teacher_schedule(teacher_name)
            elif choice == "11":
                student_name = input("Введіть ім'я учня: ")
                self.display_student_schedule(student_name)
            elif choice == "12":
                student_name = input("Введіть ім'я учня: ")
                self.add_student_schedule(student_name)
            elif choice == "13":
                self.daily_journal_menu()
            elif choice == "14":
                print("Наша компанія займається цією програмою, щоб вона допомогла учням і вчителям дізнаватися їх розклад, оцінки і все інше, що потрібно для школи. Якщо у вас є які-небудь питання, напишіть на пошту: sandy.tuor.2024@gmail.com")
            elif choice == "15":
                print("Ліцей Імені Стіва Джобса — загальноосвітній навчальний заклад; гімназія в Івано-Франківську. Учасник Всеукраїнського конкурсу «100 найкращих шкіл України». За результатами ЗНО з української мови та літератури в 2008, 2009 та у 2015 роках займала І місце серед шкіл України.")
            elif choice == "16":
                print("Вихід з програми. До побачення!")
                return
            else:
                print("Невірний вибір. Будь ласка, введіть число від 1 до 16.")

if __name__ == "__main__":
    school_schedule = SchoolSchedule()
    if hasattr(school_schedule, 'main_menu') and callable(getattr(school_schedule, 'main_menu')):
        school_schedule.main_menu()
    else:
        print("Об'єкт SchoolSchedule не має методу main_menu.")
