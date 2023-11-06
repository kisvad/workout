from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
class RoutineCreateView(LoginRequiredMixin, CreateView):
    pass

class RoutineUpdateView(LoginRequiredMixin, UpdateView):
    pass

class RoutineDeleteView(LoginRequiredMixin, DeleteView):
    pass

class RoutineDetailView(DetailView):
    pass

class RoutineListView(ListView):
    pass
