from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.contact),
    path('api/chart/data', views.ChartData.as_view(), name='home'),
    path('charts', views.charts),
]
