from django.db import models
#from django.contrib.auth.models import User
from users.models import CustomUser


# Create your models here.

class Vacancy(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    position=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=4000,null=True)
    salary=models.IntegerField(null=True)
    experience=models.IntegerField(null=True)
    Location=models.CharField(max_length=2000,null=True)
    class Meta:
        verbose_name_plural = "vacancies"
    def __str__(self):
        return self.name


class Candidate(models.Model):
    category=(
        ('Male','male'),
        ('Female','female'),
    )
    name=models.CharField(max_length=200,null=True)
    dob=models.DateField(null=True)
    gender= models.CharField(max_length=200,null=True,choices=category)
    mobile= models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)
    resume=models.FileField(null=True)
    vacancy=models.ManyToManyField(Vacancy,blank=True)
    def __str__(self):
        return self.name