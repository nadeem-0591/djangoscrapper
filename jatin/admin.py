# from django.contrib import admin

# from jatin.models import Property
# from django.contrib import admin

# class PropertyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'cost', 'property_type', 'area', 'link')

# admin.site.register(Property, PropertyAdmin)
from django.contrib import admin
from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'property_type') 

# Register the Property model with the custom admin class
admin.site.register(Property, PropertyAdmin)