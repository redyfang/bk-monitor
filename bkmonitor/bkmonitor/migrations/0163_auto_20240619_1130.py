# Generated by Django 3.2.15 on 2024-06-19 03:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bkmonitor', '0162_rebuild_strategy_priority_group_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dutyplan',
            name='is_effective',
            field=models.IntegerField(default=0, verbose_name='是否有效'),
        ),
        migrations.AlterField(
            model_name='dutyplan',
            name='user_group_id',
            field=models.IntegerField(verbose_name='关联的告警组'),
        ),
        migrations.AddIndex(
            model_name='dutyplan',
            index=models.Index(
                fields=['user_group_id', 'is_effective', 'finished_time'], name='bkmonitor_d_user_gr_2ff4d0_idx'
            ),
        ),
    ]
