# Generated by Django 4.1.1 on 2022-09-22 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_alter_autobrand_options_alter_automodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerauto',
            name='is_published',
            field=models.BooleanField(blank=True, default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='ownerauto',
            name='photo',
            field=models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
