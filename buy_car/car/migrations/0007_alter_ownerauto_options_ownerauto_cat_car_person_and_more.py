# Generated by Django 4.1.1 on 2022-10-01 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car', '0006_autobrand_sign_auto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ownerauto',
            options={'ordering': ['-time_create'], 'verbose_name': 'Продающаяся машина', 'verbose_name_plural': 'Продающаяся машина'},
        ),
        migrations.AddField(
            model_name='ownerauto',
            name='cat_car_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AlterField(
            model_name='ownerauto',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание авто'),
        ),
        migrations.AlterField(
            model_name='ownerauto',
            name='name_owner',
            field=models.CharField(max_length=250, verbose_name='Имя Фамилия'),
        ),
    ]