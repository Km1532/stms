import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_schedule_project.settings')
application = get_wsgi_application()
from school_schedule_app.models import Subject, Teacher, Class, Student

class SchoolSchedule:
    def display_subjects(self):
        subjects = Subject.objects.all()
        print("Subjects:")
        for subject in subjects:
            print(f"- {subject}")

    def display_teachers(self):
        teachers = Teacher.objects.all()
        print("\nTeachers:")
        for teacher in teachers:
            print(f"- {teacher}")

    def display_classes(self):
        classes = Class.objects.all()
        print("\nClasses:")
        for class_obj in classes:
            print(f"- {class_obj}")

    def display_students(self):
        students = Student.objects.all()
        print("\nStudents:")
        for student in students:
            print(f"- {student}")

if __name__ == "__main__":
    school_schedule = SchoolSchedule()
    school_schedule.display_subjects()
    school_schedule.display_teachers()
    school_schedule.display_classes()
    school_schedule.display_students()