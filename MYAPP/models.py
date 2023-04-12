from django.db import models

# Create your models here.

class Student(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    Age=models.IntegerField()
    phone_number=models.IntegerField()

    class Meta:
        db_table: "Student"

    def __str__(self):
        return self.firstname + ' ' +self.lastname
