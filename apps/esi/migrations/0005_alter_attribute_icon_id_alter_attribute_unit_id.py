# Generated by Django 5.2.3 on 2025-07-02 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esi', '0004_type_capacity_type_description_type_graphic_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='icon_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Icon ID'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='unit_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Unit ID'),
        ),
    ]
