
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('items/', views.ItemListView.as_view(), name='item-list'),
    path('items/<int:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('items/add/', views.ItemCreateView.as_view(), name='item-add'),
    path('items/<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item-edit'),
    path('items/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item-delete'),
    path('contact/', views.contact_view, name='contact'),
    path('api/items/', views.api_items, name='api-items'),
]
