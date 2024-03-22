from django.contrib import admin
from .models import Drink

# lets register our Drink model to be accessible in admin dashboard

admin.site.register(Drink)
