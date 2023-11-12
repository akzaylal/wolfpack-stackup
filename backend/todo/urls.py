from django.urls import path
from .views import TaskListView,TaskDetailView

urlpatterns = [
    path('create/',TaskListView.as_view(),name='create'),
    path('list/',TaskListView.as_view(),name='list'),
    path('update/<int:pk>/',TaskDetailView.as_view(),name='update'),
    path('delete/<int:pk>/',TaskDetailView.as_view(),name='delete'),
]