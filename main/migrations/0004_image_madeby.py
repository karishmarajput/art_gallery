# Generated by Django 3.2.8 on 2022-03-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_category_squareimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='madeBy',
            field=models.TextField(blank=True, null=True),
        ),
    ]
