# Generated by Django 5.1 on 2024-08-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0004_alter_investment_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
