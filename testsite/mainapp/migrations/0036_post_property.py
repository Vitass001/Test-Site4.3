# Generated by Django 3.2.7 on 2023-04-27 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0035_post_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='property',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
