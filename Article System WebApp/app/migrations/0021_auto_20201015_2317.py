# Generated by Django 3.1.2 on 2020-10-15 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20201015_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='article_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_sell', to='app.buy'),
        ),
    ]