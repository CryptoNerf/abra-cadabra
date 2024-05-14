from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='buypage'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]