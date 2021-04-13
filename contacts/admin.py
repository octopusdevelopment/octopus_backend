from django.contrib import admin
from .models import GeneralContact, Subscription, SubScription_Category, Demo


@admin.register(GeneralContact)
class GeneralContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullName', 'email', 'phone', 'subject', 'treated']
    list_editable = ['treated', 'email', 'phone', 'fullName']


@admin.register(SubScription_Category)
class SubScription_Category(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_editable = ['name', 'price']

@admin.register(Subscription)
class Subscription(admin.ModelAdmin):
    list_display = ['id', 'fullName', 'category', 'email', 'phone', 'date_start', 'date_end']
    list_editable = ['fullName', 'email', 'phone']


@admin.register(Demo)
class Demo(admin.ModelAdmin):
    list_display = ['id', 'fullName', 'category', 'email', 'phone', 'date_start', 'date_end']
    list_editable = ['fullName', 'email', 'phone']