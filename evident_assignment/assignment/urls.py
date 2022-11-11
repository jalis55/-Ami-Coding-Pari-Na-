from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_login,name='login'),
    path('signup',views.signup,name='signup'),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout',views.logoutuser,name='logout'),
    path('api-data',views.api_data,name="api_data"),
]
