# Generated by Django 5.0.6 on 2024-06-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0023_alter_kyc_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kyc',
            old_name='last_name',
            new_name='ccode',
        ),
        migrations.RenameField(
            model_name='kyc',
            old_name='first_name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='kyc',
            old_name='valid_id_back',
            new_name='idback',
        ),
        migrations.RenameField(
            model_name='kyc',
            old_name='valid_id_front',
            new_name='idfront',
        ),
        migrations.RenameField(
            model_name='kyc',
            old_name='phone_number',
            new_name='lname',
        ),
        migrations.RemoveField(
            model_name='kyc',
            name='country_code',
        ),
        migrations.AddField(
            model_name='kyc',
            name='pnumber',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='country',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]