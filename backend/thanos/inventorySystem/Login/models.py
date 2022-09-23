from http.client import LENGTH_REQUIRED
from django.db import models

# After finish on the models, type "python3 manage.py makemigrations [appName]"
# Then will see a "0001_initial.py" file under migrations file. This tell's the change to the database
# Finally need to type "python3 manage.py migrate [appName]", this will push the change to database
# Create your models here.
ROLE = (
    ('Admin', 'Admin'),
    ('General', 'General')
)

class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=16)
    email = models.EmailField()
    firstName = models.CharField(max_length=8, blank=True)
    lastName = models.CharField(max_length=8, blank=True)
    password = models.CharField(max_length=32)
    role = models.CharField(max_length=20, choices=ROLE, null=False, blank=False,default="General")
    contactNumber = models.CharField(max_length=500, blank=True)
    accountCreatTime = models.DateTimeField(auto_created=True)
    lastLoginTime = models.DateTimeField(auto_created=True)
    Admin = models.JSONField(null=True,blank=True)
    General = models.JSONField(null=True,blank=True)    

    # to show name of the User when called.
    def __str__(self) -> str:
        return self.userName

