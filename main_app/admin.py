from django.contrib import admin

#import models
from .models import Cat, CatToy

# Register your models here.
admin.site.register(Cat)
admin.site.register(CatToy)
