# Generated by Django 5.0.3 on 2024-03-20 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0016_deposit_capital_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='currency',
            field=models.CharField(default='$', max_length=200),
        ),
    ]
