# Generated by Django 2.0 on 2017-12-29 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20171228_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(related_name='friends_of', to='core.Person'),
        ),
    ]