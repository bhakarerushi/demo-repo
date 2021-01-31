from django.urls import path
from .views import first_api,SecondApi,first_django_view
urlpatterns =[
    path('first/', first_api, name='first-api'),
    path('second/', SecondApi.as_view(), name='second-api'),
    path('fdv/', first_django_view, name='first_django_view'),
]