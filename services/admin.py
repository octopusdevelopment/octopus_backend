from django.contrib import admin
from .models import  Service, ServiceContent, ServiceCategory

class ServiceContentAdmin(admin.StackedInline):
    model = ServiceContent
    extra = 0

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceContentAdmin]
    list_display = ['id', 'title', 'show', 'show_home']
    
    list_editable = ['show', 'show_home']
    exclude = ['slug']
    class Meta:
       model = Service



@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
     list_display = ['id', 'name', 'icon']
     exclude = ['slug']
     class Meta:
        model = ServiceCategory

