from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<uuid>',views.article,name='article'),
    path('article/<uuid>/comment',views.add_comment,name='add-comment')
]