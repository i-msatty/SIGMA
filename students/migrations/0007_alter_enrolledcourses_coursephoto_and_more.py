# Generated by Django 4.2.5 on 2023-11-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_enrolledcourses_students_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolledcourses',
            name='coursePhoto',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='students',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='Studnetsphotos/%Y/%m/%d/'),
        ),
    ]
