# Generated by Django 5.0.4 on 2024-04-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Renters', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]