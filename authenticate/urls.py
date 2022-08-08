from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password', views.change_password, name='change_password'),
    path('paid', views.paid, name='paid'),
    path('bitcoin/', views.bitcoin, name='bitcoin'),
    path('blockchain/', views.blockchain, name='blockchain'),
    path('terra/', views.terra, name='terra'),
    path('questions/', views.questions, name='questions'),


    

]
