from django.db import models

# Create your models here.


class ContactMessage(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name
