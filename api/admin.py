from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Login
from .models import Register

# Register your models here.
admin.site.register(Login)
admin.site.register(Register)