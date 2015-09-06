from django.contrib import admin
from .models import server
from .models import volume
# Register your models here.

class serverAdmin(admin.ModelAdmin):
    list_display = ('name', 'ipaddress')


admin.site.register(server, serverAdmin)
