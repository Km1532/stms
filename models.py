from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=255)

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Class(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    class_obj = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)    
    day = models.CharField(max_length=20)
    time = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.subject.name} ({self.day}, {self.time}, вчитель: {self.teacher.name})"


class Student(models.Model):
    name = models.CharField(max_length=255)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

class Lesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, default=1, null=True)
    day = models.CharField(max_length=20)
    time = models.CharField(max_length=10)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.subject.name} ({self.day}, {self.time}, вчитель: {self.teacher.name})"

