# Generated by Django 2.0 on 2017-12-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False, verbose_name='index')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
        ),
    ]