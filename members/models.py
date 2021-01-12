from django.db import models

from descuentosApp.models import Country, Province, City, University, Guide


from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    
    date = models.DateField(null=True, blank=True)
    
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex'))
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    country =  models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)

    PREFIX_CHOICES = (('Spain', '+34'), ('France', '+33'), ('Germany', '+49'))
    phone_prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES, blank=True)
    phone = models.IntegerField(null=True)
    STUDENT_CHOICES = (('University', 'Academic'), ('Au-P', 'Au Pair'), ('M', 'Master'), ('P', 'Practices'))
    studentType = models.CharField(max_length=10, choices=STUDENT_CHOICES)
    cityOrigin1 =  models.CharField(max_length=10, blank=True)
    cityDestination1 =  models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    cityDestination2 =  models.CharField(max_length=50, blank=True)
    cityDestination3 =  models.CharField(max_length=50, blank=True)
    universityOrigin =  models.CharField(max_length=50, blank=True)
    universityDestination =  models.ForeignKey(University, on_delete=models.CASCADE, blank=True, null=True)
    studies =  models.CharField(max_length=50, blank=True)
    course =  models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)