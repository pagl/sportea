from django.db import models

class Sport (models.Model):
    name = models.CharField(max_length=25)
    app_name = models.CharField(max_length=25)
    logo = models.ImageField(upload_to="sport")

    def __str__ (self):
        return self.name
