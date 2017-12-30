# Generated by Django 2.0 on 2017-12-28 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171228_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fruit',
            name='id',
        ),
        migrations.RemoveField(
            model_name='vegetables',
            name='id',
        ),
        migrations.AlterField(
            model_name='fruit',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='vegetables',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='name'),
        ),
    ]