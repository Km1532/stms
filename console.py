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
            print(f"- {subject}")

    def display_teachers(self):
        teachers = Teacher.objects.all()
        print("\nВчителі:")
        for teacher in teachers:
            print(f"- {teacher}")

    def display_classes(self):
        classes = Class.objects.all()
        print("\nКласи:")
        for class_obj in classes:
            print(f"- {class_obj}")

    def display_students(self):
        students = Student.objects.all()
        print("\nУчні:")
        for student in students:
            print(f"- {student}")

    def add_subject(self, name):
        subject = Subject(name=name)
        subject.save()
        print(f"Предмет {name} додано успішно.")

    def add_teacher(self, name, subject_name):
        try:
            subject = Subject.objects.get(name=subject_name)
            teacher = Teacher(name=name, subject=subject)
            teacher.save()
            print(f"Вчителя {name} додано успішно.")
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

    def display_student_schedule(self, student_name):
        try:
            student = Student.objects.get(name=student_name)
            lessons = Lesson.objects.filter(class_obj=student.class_name)
            print(f"\nРозклад уроків для учня {student_name} (клас {student.class_name}):")
            for lesson in lessons:
                print(f"- {lesson}")
        except Student.DoesNotExist:
            print(f"Учень {student_name} не знайдений.")

    def add_teacher_schedule(self, teacher_name):
        subject_name = input("Введіть назву предмету: ")
        class_name = input("Введіть назву класу: ")
        day = input("Введіть день (наприклад, Понеділок): ")

        # Додайте перевірку на коректність дня тижня
        valid_days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця"]
        if day not in valid_days:
            print("Неправильний день тижня. Введіть коректний день (Понеділок до П'ятниці).")
            return

        time = input("Введіть час (наприклад, 10:00): ")

        try:
            teacher = Teacher.objects.get(name=teacher_name)
            subject = Subject.objects.get(name=subject_name)
            class_obj = Class.objects.get(name=class_name)

            lesson = Lesson(teacher=teacher, subject=subject, class_obj=class_obj, day=day, time=time)
            lesson.save()
            print("Розклад уроку додано успішно.")
        except Teacher.DoesNotExist:
            print(f"Вчитель {teacher_name} не знайдений.")
        except Subject.DoesNotExist:
            print(f"Предмет {subject_name} не знайдений.")
        except Class.DoesNotExist:
            print(f"Клас {class_name} не знайдений.")

    def add_student_schedule(self, student_name):
        subject_name = input("Введіть назву предмету: ")
        day = input("Введіть день (наприклад, Понеділок): ")

        # Додайте перевірку на коректність дня тижня
        valid_days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця"]
        if day not in valid_days:
            print("Неправильний день тижня. Введіть коректний день (Понеділок до П'ятниці).")
            return

        time = input("Введіть час (наприклад, 10:00): ")

        try:
            student = Student.objects.get(name=student_name)
            subject = Subject.objects.get(name=subject_name)

            lesson = Lesson(student=student, subject=subject, day=day, time=time)
            lesson.save()
            print("Розклад уроку додано успішно.")
        except Student.DoesNotExist:
            print(f"Учень {student_name} не знайдений.")
        except Subject.DoesNotExist:
            print(f"Предмет {subject_name} не знайдений.")

    def display_main_menu(self):
        print("\nГоловне меню:")
        print("1. Відображення Предметів")
        print("2. Відображення Вчителів")
        print("3. Відображення Класів")
        print("4. Відображення Учнів")
        print("5. Додати предмет")
        print("6. Додати вчителя")
        print("7. Додати клас")
        print("8. Додати учня")
        print("9. Переглянути розклад для вчителя")
        print("10. Додати розклад для вчителя")
        print("11. Переглянути розклад для учня")
        print("12. Додати розклад для учня")
        print("13. Вихід")

    def main_menu(self):
        while True:
            self.display_main_menu()
            choice = input("Введіть свій вибір (1-13): ")
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
                print("Вихід з програми. До побачення!")
                break
            else:
                print("Невірний вибір. Будь ласка, введіть число від 1 до 13.")

if __name__ == "__main__":
    school_schedule = SchoolSchedule()
    school_schedule.main_menu()
