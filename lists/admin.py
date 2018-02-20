from django.contrib import admin
from lists.models import Side, Series, Ship, Type
# Register your models here.


class ShipsAdmin(admin.ModelAdmin):
    list_display = ('type', 'series', 'name', 'lenght', 'side')


admin.site.register(Series)
admin.site.register(Ship, ShipsAdmin)
admin.site.register(Type)
admin.site.register(Side)


