from django.contrib import admin

# Register your models here.

from .models import Mesto

class MestoAdmin(admin.ModelAdmin):
    list_display = [ "id", "jmeno", "zeme", "zajimavost", "pocet_obyvatel" ]
    list_filter = [ "zeme", "hlavni_mesto" ]
    ordering = ("-jmeno", )

admin.site.register(Mesto, MestoAdmin)

