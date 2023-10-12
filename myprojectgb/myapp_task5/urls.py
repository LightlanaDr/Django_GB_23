from django.urls import path
from . import views

urlpatterns = [
    path('one/<int:n>/', views.one, name='one'),
    path('two/', views.two, name='two'),
    path('three/', views.three, name='three'),
]
