from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='category_list'),

    path('category/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete':  'destroy'}),
         name='category_detail'),

    path('Product/', ProductViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='Product_list'),

    path('Product/<int:pk>/', ProductViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete':  'destroy'}),
         name='Product_detail'),

    path('Comment/', CommentViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='Comment_list'),

    path('Comment/<int:pk>/', CommentViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete':  'destroy'}),
         name='Comment_detail'),
]
