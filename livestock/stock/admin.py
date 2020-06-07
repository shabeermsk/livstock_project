from django.contrib import admin
from .models import Category, Stock, Location, Unit
from seller.models import Profile

admin.site.register(Category)
admin.site.register(Stock)
admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(Unit)
