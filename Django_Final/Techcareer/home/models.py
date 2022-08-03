from django.db import models

# Veritabanında tablolar modeller kullanılarak oluşturuldu

#Bootcamp tablosu oluşturuldu
class Bootcamp(models.Model):
    name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()


#Student tablosu içerisinde bootcamp sutünu dahil edilerek oluşturuldu.
class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthdate = models.DateField()
    email = models.EmailField()
    school = models.CharField(max_length=50)
    github = models.CharField(max_length=100000)
    linkedn = models.CharField(max_length=100000)
    definition = models.CharField(max_length=1000000000)
    bootcamp = models.CharField(max_length=50)

#Contact tablosu oluşturuldu
class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()

    def _str_(self):
        return self.name