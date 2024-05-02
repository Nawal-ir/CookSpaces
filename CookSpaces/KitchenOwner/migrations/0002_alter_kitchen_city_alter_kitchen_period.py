# Generated by Django 5.0.4 on 2024-05-01 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KitchenOwner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitchen',
            name='city',
            field=models.CharField(choices=[('الرياض', 'الرياض'), ('جدة', 'جدة'), ('الدمام', 'الدمام')], max_length=100),
        ),
        migrations.AlterField(
            model_name='kitchen',
            name='period',
            field=models.CharField(choices=[('شهري', 'شهري'), ('سنوي', 'سنوي')], max_length=100),
        ),
    ]
