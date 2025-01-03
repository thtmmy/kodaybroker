# Generated by Django 5.1.4 on 2025-01-02 08:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0032_rename_bonus_usd_deposit_bonus'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('alert', models.CharField(choices=[('sweetAlert', 'click on to show'), ('paid', 'mark as paid')], default='sweetAlert', max_length=24)),
                ('status', models.CharField(choices=[('You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.', 'You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.')], default='You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.', max_length=200, null=True)),
                ('kyc', models.CharField(choices=[('swal-2', 'swal-2'), ('swal-4', 'swal-4')], default='#swal-4', max_length=24)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
