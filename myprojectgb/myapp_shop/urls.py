from django.urls import path
from . import views

urlpatterns = [

    path('user_orders/<int:user_id>/', views.user_orders, name='user_orders'),
    path('user_orders/<int:user_id>/<int:days_ago>/', views.sorted_basket, name='sorted_basket'),

]
