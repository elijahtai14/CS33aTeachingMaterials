# 4 python3 manage.py createsuperuser
                # 5 python3 manage.py makemigrations
                # 5 python3 manage.py migrate
from django.contrib import admin
from .models import Course, Enrollment, Student

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Student)