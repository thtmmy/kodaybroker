# Generated by Django 5.0.6 on 2024-06-10 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0022_kyc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='email',
            field=models.EmailField(blank=True, max_length=250, null=True),
        ),
    ]
