from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.http import FileResponse

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


data_db = [
    {'id': 1, 'title': 'Mazda CX5', 'content':
        'История модели CX5', 'is_published': True},
    {'id': 2, 'title': 'Toyota Prado', 'content':
        'История модели Prado ', 'is_published': True},
    {'id': 3, 'title': 'Porshce Cayenne', 'content':
        'История модели Cayenne', 'is_published': False},
]


cats_db = [
    {'id': 1, 'name': 'Отзывы'},
    {'id': 2, 'name': 'Документация'},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }

    return render(request, 'auto/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Стрaница не найдена</h1>')


def about(request):
    return render(request, 'auto/about.html', {'title': 'О сайте', 'menu': menu})



def login(request):
    return HttpResponse("Авторизация")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'auto/index.html', context=data)


def serve_logo_icon(request):
    # Код для обслуживания файла nstu.ico
    # Например, если файл расположен по указанному пути
    from django.conf import settings
    import os
    icon_path = os.path.join(settings.STATIC_ROOT, 'auto/images/logo.ico')
    return FileResponse(open(icon_path, 'rb'), content_type='image/x-icon')