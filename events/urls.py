from events import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/edit/', views.event_update, name='event_update'),
    path('<int:event_id>/delete/', views.event_delete, name='event_delete'),
    path('create/', views.event_create, name='event_create'),
]
