# Generated by Django 4.1.1 on 2022-09-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Basic', '0002_auto_20220921_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]