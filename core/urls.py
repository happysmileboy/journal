from django.urls import path
from . import views

app_name="core"

urlpatterns = [
    path('', views.home),
    path('get_data', views.get_data_k)
]