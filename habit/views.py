from datetime import datetime
from pytz import timezone

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, View, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404, get_list_or_404

from django.conf.global_settings import LANGUAGE_CODE, TIME_ZONE
from .models import Habit, Daily

utc = datetime.now()
tz = timezone(TIME_ZONE)
today = utc.astimezone(tz)

# Current day
# All the habits of the user in the current day
class HomeView(LoginRequiredMixin, View):
    model = Habit
    template_name = "habits/home.html"


    def get(self, *args, **kwargs):
        context = {}
        queryset = self.model.objects.filter(user=self.request.user)
        context['habits'] = []
        context['today'] = today
        for habit in queryset:
            q = (Daily.objects.filter(habit=habit, date=today, is_active=True))
            context['habits'].append([habit, q])
        return render(self.request, self.template_name, context)

    # Create a daily with the selected habit
    # by checking the box
    def post(self,  *args, **kwargs):
        habit_id = self.request.POST["daily"]
        habit = Habit.objects.get(id=habit_id)
        q = Daily.objects.filter(habit=habit, date=today)
        if not q:
            Daily.objects.create(habit=habit, date=today)
        else:
            q[0].is_active = not (q[0].is_active)
            q[0].save() 

        return redirect('habits:home')

#  Calendar View for specific habit
class CalendarView(LoginRequiredMixin, DetailView):
    model = Habit
    context_object_name = 'habit'
    template_name = 'habits/calendar.html'

    # Get all the days the habit was done
    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        context['days'] = Daily.objects.filter(habit=self.get_object(), is_active=True)
        return context


class HabitCreateView(LoginRequiredMixin, CreateView):
    template_name = 'habits/create_habit.html'
    model = Habit
    fields = ['name', 'description']

    success_url = reverse_lazy('habits:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HabitUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'habits/habit_form.html'
    model = Habit
    fields = ['name', 'description']
    
    success_url = reverse_lazy('habits:home')

class HabitDeleteView(LoginRequiredMixin, DeleteView):
    model = Habit
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('habits:home')