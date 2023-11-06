from django.urls import path
from . import views

app_name = 'routines'

urlpatterns = [
    path('new/', views.RoutineCreateView.as_view(), name="new_routine"),
    path('<slug:slug>', views.RoutineDetailView.as_view(), name='routine_detail'),
]