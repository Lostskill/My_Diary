from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Page_Dairy)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'data', 'author', 'id')
