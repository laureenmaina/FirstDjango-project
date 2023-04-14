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
    
 class Employees(models.Model):
    Name=models.CharField(max_length=50)
    Position=models.CharField(max_length=50)
    Office=models.CharField(max_length=50)
    Age=models.IntegerField(null=True)
    Startdate=models.DateField()
    Salary=models.IntegerField()

    def  __str__(self):
        return self.Name+' '+self.Position

class Venue(models.Model):
    Venuename=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    ZipPostCode=models.IntegerField()
    ContactPhone=models.IntegerField()
    WebAddress=models.IntegerField()
    EmailAddress=models.EmailField()

    def __str__(self):
        return self.Venuename+ ' '+self.Address

class Post(models.Model):
    Author=models.IntegerField(max_length=50)
    Title=models.CharField(max_length=50)
    Text=models.TextField()
    Createddate=models.DateTimeField()
    Publisheddate=models.DateTimeField()

