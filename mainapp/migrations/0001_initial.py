# Generated by Django 4.0.2 on 2022-07-01 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FoodOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('is_open', models.BooleanField(default=False, help_text='open/closed')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('food_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.food')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_open', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('food_option', models.ManyToManyField(to='mainapp.FoodOptions')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.meal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.profile')),
            ],
        ),
        migrations.AddField(
            model_name='foodoptions',
            name='food_type_options',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.foodtype'),
        ),
    ]
