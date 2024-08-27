# Generated by Django 5.1 on 2024-08-20 21:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dividend', '0004_rename_amount_per_share_dividend_total_dividends'),
        ('investment', '0008_alter_investment_investment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dividend',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investment.investment'),
        ),
    ]
