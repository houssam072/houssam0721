from django.urls import path
from .views import CategoryViews

app_name = 'category'

urlpatterns = [
    path('add_category',CategoryViews.as_view(), name='add_category'),
    path('get_category',CategoryViews.as_view(), name='get_category'),
    path('get_category/<int:pk>',CategoryViews.as_view(), name='get_category_by_id'),
    path('delete_category/<int:pk>/', CategoryViews.as_view(), name= 'delete_category'),
]