from http.client import LENGTH_REQUIRED
from django.db import models

# After finish on the models, type "python3 manage.py makemigrations [appName]"
# Then will see a "0001_initial.py" file under migrations file. This tell's the change to the database
# Finally need to type "python3 manage.py migrate [appName]", this will push the change to database
# Create your models here.
class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=500)
    Password = models.CharField(max_length=500)
    Role = models.CharField(max_length=500)
    FirstName = models.CharField(max_length=500, blank=True)
    LastName = models.CharField(max_length=500, blank=True)
    ContactNumber = models.CharField(max_length=500, blank=True)


    # to show name of the User when called.
    def __str__(self) -> str:
        return self.Username
