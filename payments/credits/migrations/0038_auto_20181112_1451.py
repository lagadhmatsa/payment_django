# Generated by Django 2.1.2 on 2018-11-12 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0037_auto_20181112_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_redeem',
            name='transaction_id',
            field=models.CharField(default='00C02A31D1EC', max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='A0BC5C3F104C', max_length=14, unique=True),
        ),
    ]
