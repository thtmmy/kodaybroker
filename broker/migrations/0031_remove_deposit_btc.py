# Generated by Django 5.1.4 on 2025-01-02 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0030_rename_ccode_kyc_country_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='btc',
        ),
    ]
