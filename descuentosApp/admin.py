from django.contrib import admin
from .models import Country, Province, City, University, Guide
from members.models import User
# Register your models here.

admin.site.register(User)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(University)
admin.site.register(Guide)
