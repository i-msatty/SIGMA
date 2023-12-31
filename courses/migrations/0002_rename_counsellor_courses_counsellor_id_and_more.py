# Generated by Django 4.2.5 on 2023-11-13 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='counsellor',
            new_name='counsellor_id',
        ),
        migrations.AddField(
            model_name='courses',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='courses',
            name='image',
            field=models.ImageField(blank=True, upload_to='Coursesphotos/%Y/%m/%d/'),
        ),
    ]
