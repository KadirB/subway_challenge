# Generated by Django 4.0.2 on 2022-07-01 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_order_food_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='food_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.foodoptions'),
        ),
    ]