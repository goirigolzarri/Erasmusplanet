from django.db import models

from descuentosApp.models import Country, Province, City, University, Guide


from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    
    date = models.DateField(default="2020-01-01")
    
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex'))
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=False, default=False)

    COUNTRY_CHOICES = (('Spain', 'Spain'), ('France', 'France'), ('Germany', 'Germany'))
    country = models.CharField(max_length=10, choices=COUNTRY_CHOICES, blank=True, default=False)

    PREFIX_CHOICES = (('Spain', '+34'), ('France', '+33'), ('Germany', '+49'))
    phone_prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES, blank=True, default=False)
    phone = models.IntegerField(null=True)
    STUDENT_CHOICES = (('1', 'Academic'), ('2', 'Au Pair'), ('3', 'Master'), ('4', 'Practices'))
    studentType = models.CharField(max_length=10, choices=STUDENT_CHOICES, null=True)
    cityOrigin1 =  models.CharField(max_length=10, blank=True, null=True)
    cityDestination1 =  models.CharField(max_length=50, blank=True, null=True)
    cityDestination2 =  models.CharField(max_length=50, blank=True, null=True)
    cityDestination3 =  models.CharField(max_length=50, blank=True, null=True)
    universityOrigin =  models.CharField(max_length=50, blank=True, null=True)
    universityDestination =  models.CharField(max_length=50, blank=True, null=True)
    studies =  models.CharField(max_length=50, blank=True)
    course =  models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True, null=True)