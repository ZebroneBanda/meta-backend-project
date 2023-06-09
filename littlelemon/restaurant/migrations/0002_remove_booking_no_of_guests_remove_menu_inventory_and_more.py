# Generated by Django 4.2.2 on 2023-06-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='no_of_guests',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='inventory',
        ),
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
