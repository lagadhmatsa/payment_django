# Generated by Django 2.1.2 on 2018-11-10 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credits', '0026_auto_20181110_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending_transactions',
            name='transaction_id',
            field=models.CharField(default='C805B49AC3', max_length=14, unique=True),
        ),
    ]
