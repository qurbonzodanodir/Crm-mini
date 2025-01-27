from django.urls import path
from .views import CustomerApiListCreateView,CustomerApiUpdateView
urlpatterns = [
    path('create/',CustomerApiListCreateView.as_view()),
    path('update/',CustomerApiUpdateView.as_view())
]
