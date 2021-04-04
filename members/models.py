from django.db import models
from django.db.models.fields import NullBooleanField
from django.urls.base import reverse

from descuentosApp.models import Country, Province, City, University, Guide


from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    
    date = models.DateField(default="2020-01-01")
    
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Prefer not to say'))
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=False, default=False)

    country =  models.ForeignKey(Country, on_delete=models.CASCADE, default="SPAIN")
    phone = models.IntegerField(null=True, )
    prefix = models.IntegerField(null=True )
    STUDENT_CHOICES = (('1', 'Bachelor'), ('2', 'Au Pair'), ('3', 'Master'), ('4', 'Internship'))
    studentType = models.CharField(max_length=10, choices=STUDENT_CHOICES, null=True, default='')
    cityOrigin1 =  models.CharField(max_length=10, blank=True, null=True)
    cityDestination1 =  models.CharField(max_length=50, null=False)
    cityDestination2 =  models.CharField(max_length=50, blank=True)
    cityDestination3 =  models.CharField(max_length=50, blank=True)
    universityOrigin =  models.CharField(max_length=50,null= True, blank=True)
    universityDestination =  models.CharField(max_length=50, null=True, blank=True)
    studies =  models.CharField(max_length=50, null=True, blank=True)
    course =  models.CharField(max_length=50, null= True, blank=True)
    company = models.CharField(max_length=50,null= True, blank=True)


    def get_absolute_url(self):
    #return reverse('article-detail', args=(str(self.id)))
     return reverse('base')

    # def studenttypefunction(self):
    #     if self.studentType == 1:
    #         self.company = ''

    #     if self.studentType == 2:
    #         self.universityOrigin = ''
    #         self.universityDestination = ''
    #         self.course = ''
    #         self.studies = ''
    #         self.company = ''
            
    #     if self.studentType == 3:
    #         self.course = ''
    #         self.company = ''
        
    #     if self.studentType == 2:
    #         self.universityOrigin = ''
    #         self.universityDestination = ''
    #         self.course = ''
    #         self.studies = ''
        
    #     self.save()

