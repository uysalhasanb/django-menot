# Generated by Django 4.2.7 on 2023-11-28 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("moneyflow", "0007_alter_account_options_alter_category_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="transaction",
                to="moneyflow.account",
                verbose_name="account",
            ),
        ),
    ]