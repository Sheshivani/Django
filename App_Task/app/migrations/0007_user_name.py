# Generated by Django 3.1 on 2020-09-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200928_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=1, max_length=55),
            preserve_default=False,
        ),
    ]