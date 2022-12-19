from django.urls import path
from .import views
app_name = 'inventoryApp'
urlpatterns = [
    path('', views.index, name="index"),
    path('order', views.order, name="order"),
    path('products', views.products, name="products"),
    path('product_delete/<int:pk>', views.product_delete, name="product_delete"),
    path('product_edit/<int:pk>', views.product_edit, name="product_edit"),
]
