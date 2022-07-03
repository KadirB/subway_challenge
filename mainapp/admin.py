from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from mainapp.models import Profile, Meal, Food, FoodType, FoodOptions, Order


class MealAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


class OrderAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Profile)
admin.site.register(Meal, MealAdmin)
admin.site.register(Food)
admin.site.register(FoodType)
admin.site.register(FoodOptions)
admin.site.register(Order, OrderAdmin)
