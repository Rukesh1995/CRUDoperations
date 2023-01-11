from django.urls import path
from .views import ShowAllProduct, ViewProduct, CreateProduct, UpdateProduct, DeleteProduct

urlpatterns = [
    path('create-product/', CreateProduct, name='create-product'),
    path('all-product/', ShowAllProduct, name='all-product'),
    path('view-product/<int:pk>/', ViewProduct, name='view-product'),
    path('update-product/<int:pk>/', UpdateProduct, name='update-product'),
    path('delete-product/<int:pk>/', DeleteProduct, name='delete-product'),

]