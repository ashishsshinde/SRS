from django.urls import path
from api import views
from django.urls.conf import include

urlpatterns = [
    path('login/',views.login, name='login'),    
    path('username/<int:pk>',views.login_detail, name='login_detail'),
    path('list/',views.student_list, name='student_list'),
    path('show/',views.VisitData, name='VisitData'),
        

    path('register/',views.register, name='register'),
    path('register/<int:pk>',views.register_detail, name='register_detail'),
    path('list1/',views.register_list, name='register_list'),
    path('show1/',views.registerData, name='registerData'),
]