# Generated by Django 2.1.2 on 2018-11-11 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0027_auto_20181110_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='F4E16F69F4', max_length=14, unique=True),
        ),
    ]