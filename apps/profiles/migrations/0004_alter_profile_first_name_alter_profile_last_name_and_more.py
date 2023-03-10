# Generated by Django 4.1.6 on 2023-02-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_first_name_profile_last_name_profile_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, default='Ivan', max_length=50, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, default='Ivanovich', max_length=50, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='second_name',
            field=models.CharField(blank=True, default='Ivanov', max_length=50, null=True, verbose_name='Second Name'),
        ),
    ]
