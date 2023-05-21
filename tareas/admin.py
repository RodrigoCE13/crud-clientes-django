from django.contrib import admin
from .models import Cliente

class clienteAdmin(admin.ModelAdmin):
    readonly_fields=('created',)

# Register your models here
admin.site.register(Cliente, clienteAdmin)
