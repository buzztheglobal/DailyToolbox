# Generated by Django 5.2.3 on 2025-06-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(blank=True, help_text='URL the menu item links to (e.g., /about or /products/electronics/).', max_length=255, null=True),
        ),
    ]
