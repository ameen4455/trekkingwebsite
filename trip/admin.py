
from django.contrib import admin

# Register your models here.
from .models import Places,District

admin.site.register(Places)
admin.site.register(District)