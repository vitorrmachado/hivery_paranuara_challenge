# Generated by Django 2.0 on 2017-12-30 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20171229_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fruits',
            name='person',
        ),
        migrations.RemoveField(
            model_name='person',
            name='company',
        ),
        migrations.RemoveField(
            model_name='person',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='vegetables',
            name='person',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Fruits',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Vegetables',
        ),
    ]
