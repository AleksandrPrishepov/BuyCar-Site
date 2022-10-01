from django.core.paginator import Paginator

from .models import *

menu = [
    {'name':'О сайте', 'url_name': 'about'},
    {'name':'Добавить объявление', 'url_name': 'add_car'},

]

class DataMixin:
    # paginate_by = 2
    def get_user_context(self, **kwargs):
        context = kwargs
        cat = AutoBrand.objects.all()
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cat'] = cat
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context




