from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render

# Create your views here.
from mainapp.forms import OrderForm
from mainapp.models import Profile, Meal, Order

import random
import string


def get_random_password():
    random_source = string.ascii_letters + string.digits
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)

    # generate other characters
    for i in range(24):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password


@receiver(post_save, sender=User)
def imported_info_update(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance, token=get_random_password())


def home(request):
    return render(request, '../templates/index.html')


def logout_view(request):
    logout(request)
    return render(request, '../templates/index.html')


def profile(request, username, token):
    c = {}
    c['errors'] = []
    c['username'] = request.user.username

    try:
        user = User.objects.get(username=username)
        if user:
            user_profile = Profile.objects.get(user=user)
            if user_profile.token == token:
                login(request, user)
                orders = Order.objects.filter(user__user=user)
                c['token'] = user_profile.token
                c['orders'] = orders
                return render(request, '../templates/profile.html', c)

            else:
                c['errors'].append('Token is incorrect.')
                return render(request, '../templates/404.html', c)

    except:
        c['errors'].append('User does not exist. Check the link.')
        return render(request, '../templates/404.html', c)


def meal(request, name, username, token):
    c = {}
    c['errors'] = []
    c['form'] = OrderForm(request.POST)

    try:
        meal = Meal.objects.get(name=name)
        c['meal_name'] = meal.name
        c['taste'] = meal.food_type.name
    except:
        c['errors'].append('Meal does not exist. Check the link.')
        return render(request, '../templates/404.html', c)

    try:
        user = User.objects.get(username=username)
    except:
        c['errors'].append('User does not exist. Check the link.')
        return render(request, '../templates/404.html', c)

    if user:
        user_profile = Profile.objects.get(user=user)
        if user_profile.token == token:
            login(request, user)
            if meal.is_open:
                if request.method == 'POST':
                    form = OrderForm(request.POST)
                    if form.is_valid():
                        cd = form.cleaned_data
                        order = form.save(commit=False)
                        order.user = Profile.objects.get(user=user)
                        order.meal = meal
                        # for key, value in request.POST.lists():
                        #     if key in ['bread', 'vegetables', 'sauce']:
                        #         order.food_option = value
                        order.save()
                return render(request, '../templates/meal.html', c)
            else:
                c['errors'].append('Meal is closed.')
                return render(request, '../templates/404.html', c)

        else:
            c['errors'].append('Token is incorrect.')
            return render(request, '../templates/404.html', c)


def order(request, id, username, token):
    c = {}
    c['errors'] = []

    try:
        order = Order.objects.get(pk=id)
    except:
        c['errors'].append('Order does not exist. Check the link.')
        return render(request, '../templates/404.html', c)

    try:
        user = User.objects.get(username=username)
    except:
        c['errors'].append('User does not exist. Check the link.')
        return render(request, '../templates/404.html', c)

    if user:
        user_profile = Profile.objects.get(user=user)
        if user_profile.token == token:
            login(request, user)
            if order.is_open:
                c['order'] = order
                return render(request, '../templates/previous_orders.html', c)
            else:
                c['errors'].append('Order is closed.')
                return render(request, '../templates/404.html', c)

        else:
            c['errors'].append('Token is incorrect.')
            return render(request, '../templates/404.html', c)