from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_view'),
    path('<int:id>/', views.ArticleListView.as_view(), name='article_view'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),
]