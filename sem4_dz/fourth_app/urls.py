from django.urls import path
from . import views

urlpatterns = [
    path('add_product', views.product_form, name='add_product')
]
