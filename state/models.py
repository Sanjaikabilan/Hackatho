from django.db import models

# Create your models here.

class State(models.Model):
    level = (('e','Easy'),('m','Medium'),('h','Hard'))
    doms = (('1','Energy'),('2','Electronics'),('3','Electrical'),('4','AI/ML'),('5','Vehicle Development'),('6','Robotics'))
    problem = models.CharField(max_length=1000)
    domain = models.CharField(choices=doms, max_length=100)
    hardness = models.CharField(choices = level,max_length=1)

class Ques(models.Model):
    question = models.CharField(max_length=1000)

def __str__(self):
     return self.question


class Stud(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=15)
    question = models.CharField(max_length=1000)





    
