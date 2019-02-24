from django.db import models

# Create your models here.

class Person(models.Model):
  MAN = 0
  WOMEN = 1

  B4 = 0
  M1 = 1
  M2 = 2

  name = models.CharField(max_length=128)
  sex = models.IntegerField(editable=False)
  grade = models.IntegerField()
  email = models.EmailField()
  last_login = models.DateTimeField()


class Team(models.Model):
  # チームの定数
  TEAM_WIRELESS = 0
  TEAM_SENSOR = 1
  TEAM_MULTIMEDIA = 2
  TEAM_ENGLISH = 3

  person = models.ForeignKey('Person',on_delete=models.PROTECT)
  team = models.IntegerField()

