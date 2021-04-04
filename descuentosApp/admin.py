from django.contrib import admin
from .models import *
from members.models import *

from adminErasmus.models import *
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






# Modelos de Tienda
from tienda.models import *


admin.site.register(Producto)
admin.site.register(ColorProducto)


