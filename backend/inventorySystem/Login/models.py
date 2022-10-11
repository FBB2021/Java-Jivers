from http.client import LENGTH_REQUIRED
from django.db import models

# Following two used for user information verification
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

# Translate variable name to user friendly texts
from django.utils.translation import gettext_lazy as _


# After finish on the models, type "python3 manage.py makemigrations [appName]"
# Then will see a "0001_initial.py" file under migrations file. This tell's the change to the database
# Finally need to type "python3 manage.py migrate [appName]", this will push the change to database
# Create your models here.
class User(AbstractUser):
    
    ROLE = (
        ('Admin', 'Admin'),
        ('General', 'General')
    )

    UserId = models.AutoField(primary_key=True)
    role = models.CharField(max_length=20, choices=ROLE, null=False, blank=False,default="General")
    contactNumber = models.CharField(_('Contact Number'),max_length=500, blank=True)

    objects = UserManager()

    # to show name of the User when called.
    def __str__(self) -> str:
        return self.username

    # to use own user model instead of django's templete.
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        pass


    # Because the abstract user class (AbstractUser) is inherited, 
    # the following properties are not defined again.
'''
    lastLoginTime = models.DateTimeField(_('Last Login Time'),blank=True,null=True,auto_now=True)
    accountCreatTime = models.DateTimeField(_('Account Creation Time'),blank=True,null=True)
    userName = models.CharField(_('Username'),max_length=16)
    email = models.EmailField()
    firstName = models.CharField(_('First Name'),max_length=8, blank=True)
    lastName = models.CharField(_('Last Name'),max_length=8, blank=True)
    password = models.CharField(max_length=32)
'''