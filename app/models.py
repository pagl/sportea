from django.db import models

class User (models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    activation_code = models.CharField(max_length=100)
    active = models.BooleanField()

    def __str__ (self):
        return self.email


class Sport (models.Model):
    name = models.CharField(max_length=25)
    app_name = models.CharField(max_length=25)
    logo = models.ImageField()

    def __str__ (self):
        return self.name
