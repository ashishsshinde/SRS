# Generated by Django 4.0 on 2022-01-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='mobile',
            field=models.CharField(max_length=100),
        ),
    ]