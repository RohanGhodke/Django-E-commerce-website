from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='Tracker'),
    path('search/', views.search, name='Search'),
    path('product/<int:id>', views.productView, name='ProductView'),
    path('checkout/', views.checkout, name='Checkout'),
]