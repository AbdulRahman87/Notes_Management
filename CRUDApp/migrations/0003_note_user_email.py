# Generated by Django 3.2.8 on 2022-02-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDApp', '0002_user_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='user_email',
            field=models.CharField(default=None, max_length=50),
        ),
    ]