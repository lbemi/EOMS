from django.urls import path
from . import views


urlpatterns = [
    path('', views.Login),
    path('index/',views.Index_List.as_view(), name ='index'),
    path('logout/',views.logout, name='logout'),
]
