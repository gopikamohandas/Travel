from django.urls import path
from .views import*

urlpatterns = [
   
    path('',ListBlog.as_view(), name='home'),
    path('nav/',nav, name='nav'),
    path('detail/<int:pk>',DetailBlog.as_view(), name='detail'),
    path('create/',Createblog.as_view(),name='create'),
    path('edit/<int:pk>',Editblog.as_view(), name='edit'),
    path('delete/<int:pk>', Deleteblog.as_view(),name='delete')
]