# Generated by Django 2.1.2 on 2018-11-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0003_auto_20181105_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_transactions',
            name='key',
            field=models.CharField(default="3W6Q1'yMe&|JJR{9", max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='EMSpdc5284ldPE', max_length=14, unique=True),
        ),
    ]