# Generated by Django 2.1.2 on 2018-11-06 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0012_auto_20181107_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_transactions',
            name='key',
            field=models.CharField(default='ba99feeaea', max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='XlEEOsowAYEvQ', max_length=14, unique=True),
        ),
    ]
