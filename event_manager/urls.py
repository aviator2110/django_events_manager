from django.urls import include
from django.urls import path
from events import views

urlpatterns = [
    path('events/', include('events.urls')),
]
