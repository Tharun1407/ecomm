
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = "home"),
    path('Create',views.Create,name = "Create"),
     path('Employee',views.Employees,name = "Employee"),
]
