# Generated by Django 3.2.12 on 2022-06-10 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pairs', '0010_alter_userrigister_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrigister',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
