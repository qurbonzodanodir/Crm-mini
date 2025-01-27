from django.urls import path
from appeal.views import AppealApiListView,AppealApiCreateView,AppealApiUpdateView
urlpatterns = [
    path('',AppealApiListView.as_view()),
    path('create/',AppealApiCreateView.as_view()),
    path('update/<int:pk>',AppealApiUpdateView.as_view()),
]
