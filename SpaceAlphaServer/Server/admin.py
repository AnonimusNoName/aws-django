from django.contrib import admin

from .models import users, HWID

admin.site.register(users)
admin.site.register(HWID)