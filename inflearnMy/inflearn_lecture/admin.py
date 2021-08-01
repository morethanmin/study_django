from django.contrib import admin
from .models import comment, lecture


class lectureAdmin(admin.ModelAdmin):
  list_display = ('pk', 'title')

class commentAdmin(admin.ModelAdmin):
  list_display = ('pk', 'lecture', 'author', 'text')

admin.site.register(lecture,lectureAdmin)
admin.site.register(comment,commentAdmin)
