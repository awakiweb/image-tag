from django.urls import path

from .views import CategoryListView, CategorySearchView, CategoryCreate, CategoryUpdate, CategoryDelete, CategoryRestore
from .views import SubcategoryListView, SubcategorySearchView, SubcategoryCreate, SubcategoryUpdate, SubcategoryDelete, SubcategoryRestore

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/search/', CategorySearchView.as_view(), name='category_search'),
    path('category/add/', CategoryCreate.as_view(), name='category_add'),
    path('category/<int:pk>/', CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDelete.as_view(), name='category_delete'),
    path('category/<int:pk>/restore/', CategoryRestore.as_view(), name='category_restore'),

    path('subcategory/', SubcategoryListView.as_view(), name='subcategory_list'),
    path('subcategory/search/', SubcategorySearchView.as_view(), name='subcategory_search'),
    path('subcategory/add/', SubcategoryCreate.as_view(), name='subcategory_add'),
    path('subcategory/<int:pk>/', SubcategoryUpdate.as_view(), name='subcategory_update'),
    path('subcategory/<int:pk>/delete/', SubcategoryDelete.as_view(), name='subcategory_delete'),
    path('subcategory/<int:pk>/restore/', SubcategoryRestore.as_view(), name='subcategory_restore'),
]