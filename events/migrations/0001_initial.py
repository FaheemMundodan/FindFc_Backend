# Generated by Django 5.0.1 on 2024-02-18 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('venue', models.CharField(max_length=64)),
                ('poster', models.FileField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='50', max_length=100)),
                ('course', models.ForeignKey(default='50', on_delete=django.db.models.deletion.CASCADE, related_name='my_models', to='events.course')),
                ('Year', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='my_models', to='events.year')),
            ],
        ),
    ]
