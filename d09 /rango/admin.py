from django.contrib import admin
from rango.models import Students


class Stu_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Students, Stu_admin)