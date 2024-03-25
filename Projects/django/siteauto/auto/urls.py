from django.urls import path, register_converter
from auto import views, converters
from auto.views import serve_auto_icon

urlpatterns = [
    path('', views.index, name='home'),
    path('static/auto/images/logo.ico', serve_auto_icon, name='serve_logo_icon'),
]


register_converter(converters.FourDigitYearConverter, "year4")
