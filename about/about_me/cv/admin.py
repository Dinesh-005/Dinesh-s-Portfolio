from django.contrib import admin
from .models import data

class MemberAdmin(admin.ModelAdmin):
 list_display=("name","email","contactno","subject","message",)

admin.site.register(data,MemberAdmin)

