# Generated by Django 3.2.8 on 2022-04-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_image_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date_created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]