# Generated by Django 3.2.20 on 2023-11-28 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plagiatLocal', '0002_documentform_typedoc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentform',
            name='typedoc',
            field=models.CharField(max_length=100),
        ),
    ]
