# Generated by Django 2.1.2 on 2018-11-05 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0008_auto_20181105_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_transactions',
            name='key',
            field=models.CharField(default='c8FEV`L7/h:9,]#^i&', max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='6Hqow6Dc6m48I', max_length=14, unique=True),
        ),
    ]
