# Generated by Django 3.2.12 on 2022-05-19 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pairs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrigister',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.PositiveIntegerField(default=170)),
                ('weight', models.PositiveIntegerField(default=70)),
                ('gender', models.CharField(max_length=20)),
                ('pair_gender', models.CharField(max_length=20)),
                ('photo', models.URLField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pairs.userrigister')),
            ],
        ),
    ]
