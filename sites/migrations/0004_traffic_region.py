# Generated by Django 3.2 on 2021-06-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_traffic_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='traffic',
            name='region',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
