from django.urls import path
from myapp import views

urlpatterns = [
    path('home/', views.home_func,name='home'),
    path('Register/',views.register_view,name='register_name'),
    
]