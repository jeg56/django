# Generated by Django 2.2.9 on 2020-01-30 09:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_test'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='test',
            new_name='TestTable',
        ),
    ]
