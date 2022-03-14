from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class UserC(AbstractUser):
    full_name = models.CharField(max_length=350)

    def save(self, *args, **kwargs):
        full_name = self.first_name + ' ' + self.last_name

        super(UserC, self).save(*args, **kwargs)