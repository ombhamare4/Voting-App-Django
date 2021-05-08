from django.db import models
# Create your models here.
class pollQuetions(models.Model):
    pollquetion=models.CharField(max_length=120)
    option1=models.CharField(max_length=120)
    option2=models.CharField(max_length=120)
    option3=models.CharField(max_length=120)
    
    option1_count=models.IntegerField(default=0)
    option2_count=models.IntegerField(default=0)
    option3_count=models.IntegerField(default=0)

    def __str__(self):
        return str(self.pollquetion)

    def total(self):
        return self.option1_count+self.option2_count+self.option3_count
