from re import I
from django.shortcuts import render
from django.views.generic import ListView, View, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, get_list_or_404

from django.conf.global_settings import LANGUAGE_CODE, TIME_ZONE
from .models import Habit, Daily




# Current day
# All the habits of the user in the current day
class HomeView(LoginRequiredMixin, ListView):
    model = Habit
    template_name = "habits/home.html"
    context_object_name = "habits"


    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # Create a daily with the selected habit
    # by checking the box
    def post(self):
        pass


#  Calendar View for specific habit
class CalendarView(LoginRequiredMixin, DetailView):
    model = Habit
    context_object_name = 'habit'
    template_name = 'habits/calendar.html'

    # Get all the days the habit was done
    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        context['days'] = Daily.objects.filter(habit=self.get_object())
        return context


class HabitCreateView(LoginRequiredMixin, CreateView):
    template_name = 'habits/create_habit.html'
    model = Habit
    fields = ['name', 'description']

class HabitUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'habits/habit_form.html'
    model = Habit
    fields = ['name', 'description']
