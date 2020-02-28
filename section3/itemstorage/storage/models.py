from django.db import models


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__ (self):
        return (f"Student {self.id}: {self.name}")

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)

    def __str__ (self):
        return (f"Course {self.id}: {self.title}")

class Enrollment(models.Model):
    id = models.AutoField(primary_key=True)
    
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name = "courses")
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name = "students")

    def __str__ (self):
        return (f"Course {self.course_id}: Student{self.student_id}")