# Generated by Django 5.1 on 2024-10-04 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0004_alter_profile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contact_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
