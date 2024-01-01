from django.urls import path
from . import views

urlpatterns = [
    path('',views.cart_view,name='cart-view'),
    path('add/',views.cart_add,name='cart-add'),
    path('delete/',views.cart_delete,name='cart-delete'),
    path('update/',views.cart_update,name='cart-update'),
    ]

