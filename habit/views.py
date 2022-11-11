from django.shortcuts import render
from django.views.generic import ListView, View, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Habit, Daily


# Current day
# All the habits of the user in the current day
class HomeView(ListView, LoginRequiredMixin):
    model = Habit
    template_name = "habits/home.html"
    context_object_name = "habits"

    redirect_field_name = ""

    def get_queryset(self, *args, **kwargs):
        queryset = get_list_or_404(self.model, user=self.request.user)
        return queryset

    # Create a daily with the selected habit
    # by checking the box
    def post(self):
        pass


#  Calendar View for specific habit
class CalendarView(DetailView, LoginRequiredMixin):
    model = Habit
    context_object_name = 'habit'
    template_name = 'habits/calendar.html'

    # Get all the days the habit was done
    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        context['days'] = get_list_or_404(Daily, habit=self.get_object())
        return context

class HabitCreateView(CreateView, LoginRequiredMixin):
    model = Habit
    fields = ['name', 'description']

class HabitUpdateView(UpdateView, LoginRequiredMixin):
    model = Habit
    fields = ['name', 'description']
