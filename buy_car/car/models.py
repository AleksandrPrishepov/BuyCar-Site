from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class AutoBrand(models.Model):
    brand = models.CharField(max_length=250,verbose_name='Марка')
    sign_auto = models.ImageField(upload_to='uploads/sign_auto/', verbose_name='фото значка', blank=True)
    slug_brand = models.SlugField(max_length=50, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('brand_cars', kwargs={'car_slug':self.slug_brand})

    def get_absolute_url_2(self):
        return reverse('owner_car', kwargs={'one_car_slug':self.slug_brand})

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марка автомобиля'
        ordering = ['brand']

class AutoModel(models.Model):
    model = models.CharField(max_length=250, verbose_name='Модель')
    cat_car_brand = models.ForeignKey(AutoBrand, on_delete=models.PROTECT, verbose_name='Категория марки')
    slug_model = models.SlugField(max_length=50, verbose_name='URL модели')

    def get_absolute_url(self):
        return reverse('about_car', kwargs={'about_car_slug':self.slug_model})

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модель автомобиля'
        ordering = ['model']

class OwnerAuto(models.Model):
    USD = 'USD'
    EUR = 'EUR'
    RUB ='RUB'
    BYN = 'BYN'
    CURRENSY = [
        (USD, 'USD'),
        (EUR, 'EUR'),
        (RUB, 'RUB'),
        (BYN, 'BYN')
    ]
    name_owner = models.CharField(max_length=250, verbose_name='Имя Фамилия')
    brand_owner = models.CharField(max_length=250, verbose_name='Марка прдавца')
    model_owner = models.CharField(max_length=250, verbose_name='Модель продавца')
    description = models.TextField(blank=True, verbose_name= 'Описание авто')
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='Фото', blank=True)
    year_old = models.IntegerField(verbose_name='Год выпуска')
    prise = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена', null=True)
    currency = models.CharField(max_length=50, choices=CURRENSY, default=USD, verbose_name='Валюта')
    slug_owner = models.SlugField(max_length=50, verbose_name='URL владельца')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация', blank=True)
    cat_car_model = models.ForeignKey(AutoModel, on_delete=models.PROTECT, verbose_name='модель авто', null=True)
    cat_car_brand = models.ForeignKey(AutoBrand, on_delete=models.PROTECT, verbose_name='марка авто', null=True)
    cat_car_person= models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='пользователь', null=True)


    def get_absolute_url(self):
        return reverse('about_one_car', kwargs={'about_one_car_id':self.pk})

    def __str__(self):
        return self.brand_owner

    class Meta:
        verbose_name = 'Продающаяся машина'
        verbose_name_plural = 'Продающаяся машина'
        ordering = ['-time_create']













