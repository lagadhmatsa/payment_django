# Generated by Django 2.1.2 on 2018-11-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0005_auto_20181105_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_transactions',
            name='key',
            field=models.CharField(default=None, max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='sihO1bXiojAjFsF', max_length=14, unique=True),
        ),
    ]