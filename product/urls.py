from django.urls import path

from .views import CategoryListView, CategorySearchView, CategoryCreate, CategoryUpdate, CategoryDelete, CategoryRestore

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/search/', CategorySearchView.as_view(), name='category_search'),
    path('category/add/', CategoryCreate.as_view(), name='category_add'),
    path('category/<int:pk>/', CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDelete.as_view(), name='category_delete'),
    path('category/<int:pk>/restore/', CategoryRestore.as_view(), name='category_restore'),
]