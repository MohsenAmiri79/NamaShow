# Generated by Django 3.2.5 on 2022-01-08 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='nameOf',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]