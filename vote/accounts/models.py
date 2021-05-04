from django.db import models

# Create your models here.
class pollQuetions(models.Model):
    pollquetion=models.CharField(max_length=20)
    option1=models.CharField(max_length=20)
    option2=models.CharField(max_length=20)
    option3=models.CharField(max_length=20)

    def __str__(self):
        return str(self.pollquetion)
