# Generated by Django 5.2.3 on 2025-07-01 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esi', '0003_attribute_typeattribute'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='capacity',
            field=models.FloatField(blank=True, default=0, verbose_name='Capacity'),
        ),
        migrations.AddField(
            model_name='type',
            name='description',
            field=models.TextField(default='', verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='type',
            name='graphic_id',
            field=models.IntegerField(blank=True, default=0, verbose_name='Graphic ID'),
        ),
        migrations.AddField(
            model_name='type',
            name='market_group_id',
            field=models.IntegerField(blank=True, default=0, verbose_name='Market Group ID'),
        ),
        migrations.AddField(
            model_name='type',
            name='mass',
            field=models.FloatField(blank=True, default=0, verbose_name='Mass'),
        ),
        migrations.AddField(
            model_name='type',
            name='packaged_volume',
            field=models.FloatField(blank=True, default=0, verbose_name='Packaged Volume'),
        ),
        migrations.AddField(
            model_name='type',
            name='portion_size',
            field=models.FloatField(blank=True, default=0, verbose_name='Portion Size'),
        ),
        migrations.AddField(
            model_name='type',
            name='radius',
            field=models.FloatField(blank=True, default=0, verbose_name='Radius'),
        ),
        migrations.AddField(
            model_name='type',
            name='volume',
            field=models.FloatField(blank=True, default=0, verbose_name='Packaged'),
        ),
    ]
