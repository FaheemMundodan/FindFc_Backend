# Generated by Django 5.0.1 on 2024-02-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_material_remove_mymodel_course_remove_mymodel_year_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=64)),
                ('poster', models.FileField(default='', upload_to='')),
            ],
        ),
    ]