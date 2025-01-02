# Generated by Django 4.2.5 on 2023-09-10 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('broker', '0005_rename_name_details_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, null=True)),
                ('btc', models.CharField(default='0.00', max_length=200, null=True)),
                ('profit_usd', models.CharField(default='0.00', max_length=200, null=True)),
                ('usd', models.CharField(default='0.00', max_length=200)),
                ('bonus_usd', models.CharField(default='0.00', max_length=200)),
                ('gift_cards', models.CharField(default='0.00', max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]