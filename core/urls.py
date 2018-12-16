from django.urls import path
from . import views

app_name="core"

urlpatterns = [
    path('', views.home, name='home'),
    path('middle/', views.middle, name='middle'),
    path('small/', views.small, name='small'),
    path('get_data', views.get_data_k),
    path('news/<int:pk>',views.article_detail, name='article_detail'),
]