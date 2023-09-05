from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_productos, name='listar_productos'),
    path('insertar/', views.insertar_producto, name='insertar_producto'),
    path('editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('detalle/<int:pk>/', views.ProductoDetailView.as_view(), name='detalle_producto'),
]