from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.subject.name})'

class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.class_name.name})'