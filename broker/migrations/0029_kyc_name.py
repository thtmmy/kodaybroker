# Generated by Django 5.0.6 on 2024-06-10 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0028_alter_kyc_options_rename_name_kyc_fname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kyc',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
