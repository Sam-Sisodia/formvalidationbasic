# Generated by Django 4.1.1 on 2022-09-22 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basic', '0005_alter_userregister_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='gender',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
