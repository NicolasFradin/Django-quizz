from django.contrib import admin
from .models import *

# Register your models here.
# Add your models where to show them in the Django admin panel
# 		LOCAL -> http://127.0.0.1:8000/admin/



admin.site.register(Question)
admin.site.register(Choice)