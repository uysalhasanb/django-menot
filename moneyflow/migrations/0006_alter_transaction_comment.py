# Generated by Django 4.2.7 on 2023-11-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("moneyflow", "0005_alter_account_options_alter_category_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="comment",
            field=models.CharField(
                blank=True, max_length=200, verbose_name="komment"
                ),
        ),
    ]
