# Generated by Django 4.2 on 2024-01-30 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_tag_alter_quote_options_quote_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quote',
            options={},
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='name',
        ),
    ]
