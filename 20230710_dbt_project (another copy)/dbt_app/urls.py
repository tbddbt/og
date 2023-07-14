from django.urls import path, re_path
from dbt_app import views

app_name = "dbt_app"
urlpatterns = [
    path('', views.upload, name='uplink'),
    path('save', views.save, name='save'),
]