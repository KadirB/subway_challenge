# Generated by Django 4.0.2 on 2022-07-03 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_alter_order_food_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='food_option',
        ),
    ]
