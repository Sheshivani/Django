# Generated by Django 3.1.2 on 2020-10-15 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20201015_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='article_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_article', to='app.article', unique=True),
        ),
    ]
