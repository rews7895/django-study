# Generated by Django 3.1.3 on 2020-11-22 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='deleted_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_date',
            field=models.DateTimeField(null=True),
        ),
    ]
