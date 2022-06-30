from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)


class Meal(models.Model):
    name = models.CharField(max_length=30)
    is_open = models.BooleanField(default=False, help_text="open/closed")
    created_at = models.DateTimeField(auto_now_add=True)


class FoodType(models.Model):
    name = models.CharField(max_length=30)


class FoodTypeOptions(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    option_name = models.CharField(max_length=30)


class Order(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food_type = models.ManyToManyField(FoodType)
    food_option = models.ManyToManyField(FoodTypeOptions)
    is_open = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
