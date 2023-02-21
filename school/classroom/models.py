from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} teaches {self.subject}"