from django.db import models
from django.conf import settings
from phone_field import PhoneField 


# Create your models here.
class Profile(models.Model):
    CHOICES = (('unilag', 'Unilag'), ('yabatech', 'Yabatech'), ('fce', 'Fce'))
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True)
    school = models.CharField(max_length=10, choices=CHOICES, default='Unilag')
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    phone = PhoneField(null=True, blank=False, unique=True)
    def __str__(self):        
        return 'Profile for user {}'.format(self.user.username)
