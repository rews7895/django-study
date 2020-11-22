from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('index/', views.Index.as_view(), name='index'),
    path('create/', views.create, name='create'),
    path('store/', views.store, name='store'),
    path('<int:pk>/', views.Detail.as_view(), name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # path('logout/', views.logout, name='logout'),
]