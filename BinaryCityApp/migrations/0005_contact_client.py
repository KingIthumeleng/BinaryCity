# Generated by Django 5.1.1 on 2024-09-23 17:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BinaryCityApp', '0004_rename_contact_surname_name_contact_contact_surname'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='client',
            field=models.ForeignKey(default='HIM', on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='BinaryCityApp.client'),
        ),
    ]
