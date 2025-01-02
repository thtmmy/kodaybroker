# Generated by Django 5.0.6 on 2024-06-10 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0020_remove_bitcoin_date_time_remove_bitcoin_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_name',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='account_number',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='bank_name',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='bitcoin_address',
            field=models.CharField(default=' ', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='cashapp_tag',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='ethereum_address',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='paypal_email',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='account',
            name='swift_code',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
