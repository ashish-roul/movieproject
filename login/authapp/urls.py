from django.urls import path
from . import views
app_name='authapp'
urlpatterns = [
path('',views.logininput, name='logininput'),
path('reginput',views.reginput,name='reginput'),
path('login',views.login,name='login'),
path('reg',views.reg,name='reg'),
]
