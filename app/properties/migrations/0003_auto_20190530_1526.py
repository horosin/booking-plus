# Generated by Django 2.2.1 on 2019-05-30 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_add_groups'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
        migrations.AddField(
            model_name='property',
            name='capacity',
            field=models.IntegerField(default=2),
        ),
    ]
