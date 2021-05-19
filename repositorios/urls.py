from django.urls import path
from repositorios import views

urlpatterns = [
    path('index_repositorios/', views.list_repositorio, name='index_repositorios'),
    path('create_user/', views.UserCreate.as_view(), name='create_user'),
    #path('buscar_git/', views.buscar_repositorios.as_view(), name='buscar_git'),
]
