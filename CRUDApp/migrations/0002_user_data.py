# Generated by Django 3.2.8 on 2022-02-28 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Data',
            fields=[
                ('user_email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
