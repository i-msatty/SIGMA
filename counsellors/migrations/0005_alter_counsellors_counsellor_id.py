# Generated by Django 4.2.5 on 2023-11-16 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('counsellors', '0004_alter_counsellors_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counsellors',
            name='counsellor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
