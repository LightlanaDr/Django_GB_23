from django.urls import path
from . import views

urlpatterns = [

    path('user_orders/<int:user_id>/', views.user_orders, name='user_orders'),
    path('user_orders/<int:user_id>/<int:days_ago>/', views.sorted_basket, name='sorted_basket'),
    path('create_product/', views.create_product, name='create_product'),
    path('update_product/<int:id_product>/', views.update_product, name='update_product'),
    path('created/', views.create_product, name='created'),
]
