from django.urls import path
from .views import post_list,B
urlpatterns = [
    path('a', post_list ),
    path('b', B ,name='B'),

]