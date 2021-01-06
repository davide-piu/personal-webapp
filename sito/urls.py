from django.urls import path
from . import views


app_name='sito'
urlpatterns=[
    path('',views.index,name="index"),
]

