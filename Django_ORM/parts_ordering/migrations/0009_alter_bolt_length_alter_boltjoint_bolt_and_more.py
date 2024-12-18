# Generated by Django 5.1.1 on 2024-09-13 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts_ordering', '0008_alter_order_cost_alter_order_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bolt',
            name='length',
            field=models.FloatField(verbose_name='номинальная длина, мм'),
        ),
        migrations.AlterField(
            model_name='boltjoint',
            name='bolt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='boltjoint_bolt', to='parts_ordering.bolt', verbose_name='болт'),
        ),
        migrations.AlterField(
            model_name='boltjoint',
            name='bolt_washer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='boltjoint_bolt_washer', to='parts_ordering.washer', verbose_name='шайба со стороны болта'),
        ),
        migrations.AlterField(
            model_name='boltjoint',
            name='locknut',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='boltjoint_locknut', to='parts_ordering.nut', verbose_name='контргайка'),
        ),
        migrations.AlterField(
            model_name='boltjoint',
            name='nut',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='boltjoint_nut', to='parts_ordering.nut', verbose_name='гайка'),
        ),
        migrations.AlterField(
            model_name='boltjoint',
            name='nut_washer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='boltjoint_nut_washer', to='parts_ordering.washer', verbose_name='шайба со стороны гайки'),
        ),
        migrations.AlterField(
            model_name='item',
            name='cost',
            field=models.FloatField(verbose_name='стоимость, руб'),
        ),
    ]
