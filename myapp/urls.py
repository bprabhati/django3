from django.urls import path
from myapp import views

urlpatterns = [
    path('home/', views.home_func,name='home_name'),
    path('register/',views.register_view,name='register_name'),
    path('login/',views.login_view, name="login_name"),
    path('logout/',views.logout_view, name="logout_name"),
    path('external-joke/', views.get_joke_from_external_api, name='external_joke'),
    
]