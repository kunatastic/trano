# Generated by Django 4.0.3 on 2022-03-15 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='train',
            old_name='depature',
            new_name='departure',
        ),
    ]
