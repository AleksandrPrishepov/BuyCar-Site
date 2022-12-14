# Generated by Django 4.1.1 on 2022-09-23 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_ownerauto_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerauto',
            name='cat_car_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='car.automodel', verbose_name='модель авто'),
        ),
        migrations.AlterField(
            model_name='ownerauto',
            name='cat_car_brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='car.autobrand', verbose_name='марка авто'),
        ),
        migrations.AlterField(
            model_name='ownerauto',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание автомобиля'),
        ),
    ]
