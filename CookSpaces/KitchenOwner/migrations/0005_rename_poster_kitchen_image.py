# Generated by Django 5.0.4 on 2024-04-30 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KitchenOwner', '0004_alter_kitchen_poster'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kitchen',
            old_name='poster',
            new_name='image',
        ),
    ]
