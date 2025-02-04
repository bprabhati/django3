from django.urls import path
from myapp import views

urlpatterns = [
    path('home/', views.home_func,name='home_name'),
    path('register/',views.register_view,name='register_name'),
    path('login/',views.login_view,name="login_name"),
    path('logout/',views,name="logout_name"),
    
]