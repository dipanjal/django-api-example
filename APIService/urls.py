from django.urls import path

from .views.class_based_view import Index


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<int:id>', Index.as_view(), name='index')
]