# Generated by Django 4.0.3 on 2022-03-15 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0003_coach'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coach',
            old_name='coach_type',
            new_name='type',
        ),
        migrations.AddField(
            model_name='coach',
            name='number',
            field=models.CharField(default='GEN', max_length=10),
        ),
    ]