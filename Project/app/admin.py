from django.contrib import admin
from .models import *

# Register your models here.
class NoteAdd(admin.ModelAdmin):
    list_display=['title','user','createdate']

admin.site.register(Note,NoteAdd)