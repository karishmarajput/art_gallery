# Generated by Django 3.2.8 on 2022-04-05 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220405_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
