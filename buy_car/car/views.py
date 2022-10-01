from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from car.utils import *
from car.forms import *
from car.models import *


class Main(DataMixin, ListView):
    model = OwnerAuto
    template_name = 'car/index.html'
    context_object_name = 'owner'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

class BrandCars(DataMixin, ListView):
    model = AutoModel
    template_name = 'car/brand_cars.html'
    context_object_name = 'model_car'

    def get_queryset(self):
        return AutoModel.objects.filter(cat_car_brand__slug_brand=self.kwargs['car_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.get_queryset().exists():
            c_def = self.get_user_context(title='Главная страница',
                                          cat_one=get_object_or_404(AutoBrand, slug_brand=self.kwargs['car_slug']),
                                          cat_selected = context['cat_one'].pk)
        else:
            c_def = self.get_user_context(title='Главная страница',
                                          cat_one=get_object_or_404(AutoBrand, slug_brand=self.kwargs['car_slug']),
                                          cat_selected=context['model_car'][0].cat_car_brand.pk)
        return dict(list(context.items()) + list(c_def.items()))


class OwnerCar(DataMixin, ListView):
    model = OwnerAuto
    template_name = 'car/one_of_brands.html'
    context_object_name = 'owner_car'
    paginate_by = 2

    def get_queryset(self):
        return OwnerAuto.objects.filter(cat_car_brand__slug_brand=self.kwargs['one_car_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.get_queryset().exists():
            c_def = self.get_user_context(title='Главная страница',
                                          cat_selected=get_object_or_404(AutoBrand, slug_brand=self.kwargs['one_car_slug']).pk)
        else:
            c_def = self.get_user_context(title='Главная страница',
                                          cat_selected=context['owner_car'][0].cat_car_brand.pk)
        return dict(list(context.items()) + list(c_def.items()))


class AboutCar(DataMixin, ListView):
    model = OwnerAuto
    template_name = 'car/only_one_mark.html'
    context_object_name = 'cars_one_marks'
    paginate_by = 2

    def get_queryset(self):
        return OwnerAuto.objects.filter(cat_car_model__slug_model=self.kwargs['about_car_slug'])
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.get_queryset().exists():
            c_def = self.get_user_context(title='Главная страница',
                                          cat_selected=None)
        else:
            c_def = self.get_user_context(title='Главная страница',
                                          cat_selected=context['cars_one_marks'][0].cat_car_brand.pk)
        return dict(list(context.items()) + list(c_def.items()))

class AboutOneCar(DataMixin, DetailView):
    model = OwnerAuto
    template_name = 'car/about_one_car.html'
    pk_url_kwarg = 'about_one_car_id'
    context_object_name = 'about_one_auto'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница',
                                      cat_selected=context['about_one_auto'].cat_car_brand_id)
        return dict(list(context.items()) + list(c_def.items()))

class AddCar(DataMixin, CreateView):
    form_class = AddCarForm
    template_name = 'car/add_car.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

class Register(DataMixin,CreateView):
    form_class = RegisterUserForm
    template_name = 'car/register.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница', cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')

class Login(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'car/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница', cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main')

def logout_user(request):
    logout(request)
    return redirect('main')

class About(DataMixin, TemplateView):
    template_name = 'car/about_site.html'
    hard_skils = ('Python', 'Django', 'ORM Django', 'СУБД: SQLite')
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница', hard_skils=self.hard_skils)
        return dict(list(context.items()) + list(c_def.items()))

class Connect(FormView):
    pass
