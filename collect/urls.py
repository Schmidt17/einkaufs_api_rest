from django.urls import path
from . import views


urlpatterns = [
    path('collect/', views.CollectItem.as_view()),
    path('items/', views.ItemList.as_view()),
    path('sort/', views.SortList.as_view())
]