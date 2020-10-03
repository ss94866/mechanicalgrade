from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name='home'),
    path('login/', views.login ,name = 'login'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.logout ,name= 'logout'),
    path('status/', views.status , name = 'status'),
    path("status/sem1/", views.sem1 ,name = 'sem1'),
    path("status/sem2/", views.sem2 ,name = 'sem2'),
    path("status/sem3/", views.sem3 ,name = 'sem3'),
    path("status/sem4/", views.sem4 ,name = 'sem4'),
    path("status/sem5/", views.sem5 ,name = 'sem5'),
    path("status/sem6/", views.sem6 ,name = 'sem6'),
    path("status/sem7/", views.sem7 ,name = 'sem7'),
    path("status/sem8/", views.sem8 ,name = 'sem8'),
    path("update/sem1/", views.update1 , name = "update1"),
    path("update/sem2/", views.update2 , name = "update2"),
    path("update/sem3/", views.update3 , name = "update3"),
    path("update/sem4/", views.update4 , name = "update4"),
    path("update/sem5/", views.update5 , name = "update5"),
    path("update/sem6/", views.update6 , name = "update6"),
    path("update/sem7/", views.update7 , name = "update7"),
    path("update/sem8/", views.update8 , name = "update8"),


]
