# Generated by Django 5.1.1 on 2024-09-23 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BinaryCityApp', '0005_contact_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='client',
            field=models.ForeignKey(default='non', on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='BinaryCityApp.client'),
        ),
    ]
