from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length = 30)
    price = models.DecimalField(max_digits=30,decimal_places=3)
    date = models.DateTimeField()
    publish = models.ForeignKey(to="Publish",to_field='id',on_delete = models.CASCADE)
    authors = models.ManyToManyField(to='Author')

class Publish(models.Model):
    title = models.CharField(max_length = 30)
    addr = models.CharField(max_length = 30)

class Author(models.Model):
    name = models.CharField(max_length = 30)
    addr = models.CharField(max_length = 30)
    gf = models.OneToOneField(to='Gfriend',to_field='id',on_delete=models.CASCADE)

class Gfriend(models.Model):
    name = models.CharField(max_length =30)
    age = models.IntegerField()



class User(models.Model):
    name = models.CharField(max_length = 30)
    pwd = models.IntegerField()
    date = models.DateTimeField()
    email = models.EmailField()
