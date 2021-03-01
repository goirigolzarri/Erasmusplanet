from django.contrib import admin
from .models import Country, Province, City, University, Guide
from members.models import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class CountryAdmin(ImportExportModelAdmin):
    pass


admin.site.register(User)
admin.site.register(Country, CountryAdmin)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(University)
admin.site.register(Guide)
