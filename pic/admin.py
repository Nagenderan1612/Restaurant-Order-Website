from django.contrib import admin
from pic.models import Contact
from pic.models import Dish
from pic.models import Team,Category,Profile,Order

# Register your models here.
admin.site.site_header = "Taste & Tell | Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','added_on','is_approved']

admin.site.register(Contact, ContactAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']

admin.site.register(Category, CategoryAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']

admin.site.register(Team, TeamAdmin)

class DishAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','added_on','updated_on']




admin.site.register(Dish, DishAdmin )
admin.site.register(Profile)
admin.site.register(Order)


