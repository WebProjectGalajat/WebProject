from django.contrib import admin

# Register your models here.

from .models import Favourite_Artist, Favourite_Genre, Favourite_Song

admin.site.register(Favourite_Artist)
admin.site.register(Favourite_Song)
admin.site.register(Favourite_Genre)
