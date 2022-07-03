from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.user.username)


class Food(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name)


class FoodType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name)


class FoodOptions(models.Model):
    food_type_options = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name)


class Meal(models.Model):
    name = models.CharField(max_length=30)
    food_type = models.ForeignKey(Food, on_delete=models.CASCADE)
    is_open = models.BooleanField(default=False, help_text="open/closed")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)


class Order(models.Model):
    SIZE_CHOICES = (
        ('Small', '25'),
        ('Medium', '30'),
    )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food_option = models.ManyToManyField(FoodOptions)
    extra = models.TextField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='Small')
    oven_baked = models.BooleanField(default=False, blank=True, null=True)
    is_open = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        date = self.created_at.strftime("%d-%b-%y")
        if self.is_open:
            status = "open"
        else:
            status = "closed"
        return 'Order created at {} and status is {}'.format(date, status)