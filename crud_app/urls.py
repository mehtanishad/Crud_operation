from django.urls import path
from .views import *
from crud_app import views

urlpatterns = [
    
    path('',views.create,name='create'),
    # path('read/',views.read,name='read'),
    path('update/<int:id>/',views.edit,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    

]
