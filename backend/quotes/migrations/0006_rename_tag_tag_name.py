# Generated by Django 4.2 on 2024-01-30 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0005_rename_name_tag_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='name',
        ),
    ]
