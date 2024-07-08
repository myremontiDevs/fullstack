from django.db import models

# Create your models here.

class Adminlogin(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    logindt = models.CharField(max_length=200)
    validdt = models.CharField(max_length=55)
    permission = models.CharField(max_length=80)


    def __str__(self):
        return f"{self.fullname}"
    
class Craftsman(models.Model):
    user_id = models.CharField(max_length=255) 
    set_date = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    personal_id = models.CharField(max_length=20, unique=True) 
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    last_login = models.CharField(max_length=200)
    experience = models.CharField(max_length=210)
    salary = models.CharField(max_length=200)
    visit_salary = models.CharField(max_length=200)
    descript = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    image = models.ImageField(upload_to='dbImages')

    def __str__(self):
        return f"{self.name} {self.lastname}"

class Client(models.Model):
    user_id = models.CharField(max_length=255) 
    set_date = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    personal_id = models.CharField(max_length=20, unique=True) 
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=128) 
    last_login = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.lastname}"

    