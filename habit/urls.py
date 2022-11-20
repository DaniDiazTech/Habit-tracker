from django.urls import path
from .views import *


app_name = 'habits'
urlpatterns = [
    # User, all the habits in the current day
    path('', HomeView.as_view(), name="home"),

    # Calendar view
    path('<int:pk>/', CalendarView.as_view(), name="calendar"),

    # Create habit
    path('create/', HabitCreateView.as_view(), name="create"),

    # Update habit
    path('<int:pk>/habit', HabitUpdateView.as_view(), name="update"),
]
