# Generated by Django 2.2.5 on 2019-09-16 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
