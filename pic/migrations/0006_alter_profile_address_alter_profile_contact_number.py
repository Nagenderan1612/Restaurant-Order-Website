# Generated by Django 5.1 on 2024-10-04 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0005_profile_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
