from django.contrib import admin
from .models import SavedCredentials, SnapchatCredentials

# Register your models here.
admin.site.register(SavedCredentials)

admin.site.register(SnapchatCredentials)
