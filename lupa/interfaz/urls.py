from django.urls import path
from . import views

urlpatterns = [
    path('', views.nosotros, name='nosotros'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('prueba/', views.prueba, name='prueba'),
    path('pagina_prueba/', views.pagina_prueba, name='pagina_prueba'),
    path('cartas/crear_carta/', views.crear_carta, name='crear_carta'),
    path('cartas/modificar_carta/<int:id>/', views.modificar_carta, name='modificar_carta'),
    path('cartas/eliminar_carta/<int:id>/', views.eliminar_carta, name='eliminar_carta'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
]