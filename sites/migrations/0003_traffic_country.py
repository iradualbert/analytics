# Generated by Django 3.2 on 2021-06-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_traffic_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='traffic',
            name='country',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]