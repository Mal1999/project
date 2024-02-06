from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], null=True, blank=True)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    courses = models.ForeignKey('Course', on_delete=models.CASCADE)
    purpose = models.CharField(max_length=20, default="", null=True, blank=True)
    materials_provide = models.CharField(max_length=50, choices=[('Rocketbook', 'Rocketbook'), ('Highlighters', 'Highlighters'), ('Binders', 'Binders'), ('Backpack', 'Backpack'), ('StickyNotes', 'StickyNotes')])

class Material(models.Model):
        name = models.CharField(max_length=50)

class Department(models.Model):
    name = models.CharField(max_length=50, choices=[
        ('Science', 'Science'),
        ('Commerce', 'Commerce'),
        ('Humanities', 'Humanities'),
        ('MBA', 'MBA'),
        ('Computational Biology', 'Computational Biology')
    ])
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
