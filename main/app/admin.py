from django.contrib import admin
from .models import Profile, Trener, Client, SportProducts

# регистрируем в admin panele наши модели
admin.site.register(Profile)
admin.site.register(Trener)
admin.site.register(Client)
admin.site.register(SportProducts)
