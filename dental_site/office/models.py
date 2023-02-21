from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    heartrate = models.IntegerField(default=60, validators=[MinValueValidator(1), MaxValueValidator(300)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name} is {self.age} years old.'

#carl = Patient(first_name="Carl", last_name="Johnson", age=25, email="carl.johnson@gmail.com", phone="555-555-5555", address="123 Main St", city="Los Santos", state="CA", zip_code="12345", date_of_birth="1995-01-01")
#suzan = Patient(first_name="Suzan", last_name="Johnson", age=25, email="sujo@gmail.com", phone="555-555-5555", address="123 Main St", city="Los Santos", state="CA", zip_code="12345", date_of_birth="1995-01-01")
#mimi = Patient(first_name="Mimi", last_name="Johnson", age=25, email="mimi@gmail.com", phone="555-555-5555", address="123 Main St", city="Los Santos", state="CA", zip_code="12345", date_of_birth="1995-01-01")
#mimi.save()

# mylist = [Patient(first_name='adam',last_name='smith',age=40, email="adam.smith@gmail.com", phone="555-555-5555", address="123 Main St", city="Los Santos", state="CA", zip_code="12345", date_of_birth="1995-01-01"), 
#           Patient(first_name='karl',last_name='marx',age=40, email="karl.marx@gmail.com", phone="555-555-5555", address="123 Main St", city="Los Santos", state="CA", zip_code="12345", date_of_birth="1995-01-01") ]
# Patient.objects.bulk_create(mylist)    