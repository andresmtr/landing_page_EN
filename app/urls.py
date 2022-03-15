#Imports
from django.urls import path
from app import views
from django.conf.urls import url 


from .views import Beginning

#Import URL
urlpatterns = [

    path('',Beginning.index, name = 'index'),
    # path('union/',union.concat, name = 'union'),

]