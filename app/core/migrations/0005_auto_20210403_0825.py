# Generated by Django 3.1.7 on 2021-04-03 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='time_minitues',
            new_name='time_minutes',
        ),
    ]
