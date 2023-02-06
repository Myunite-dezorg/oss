# Generated by Django 4.1.6 on 2023-02-06 10:21

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
        migrations.AddField(
            model_name='profile',
            name='second_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Second Name'),
        ),
        migrations.AddField(
            model_name='profile',
            name='shift_work',
            field=models.BooleanField(default=0, verbose_name='Shift sched?'),
        ),
    ]
