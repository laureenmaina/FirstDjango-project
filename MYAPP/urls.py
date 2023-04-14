from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('back/', views.background),
    path('bills/', views.bills,name='bills'),
    path('images/', views.image,name='hello'),
    path('members/', views.members),
    path('student/', views.Student),
    path('', views.Employee),
    path('session/', views.setsession),
    path('sessions/', views.getsession),
    path('form/', views.form),
    path('', views.forms),

]
