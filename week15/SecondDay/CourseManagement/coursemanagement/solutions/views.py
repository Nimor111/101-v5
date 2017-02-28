from django.shortcuts import render
from django.views import generic
from datetime import datetime
from django.http import HttpResponseRedirect

from .forms import SolutionForm

from website.models import Student
from .models import Solution


# Create your views here.
class SolutionCreateView(generic.CreateView):
    form_class = SolutionForm
    template_name = 'solutions/add_solution.html'
    success_url = '/'

    def form_valid(self, form):
        solution = form.save(commit=False)
        solution.student = Student.objects.get(
            email=self.request.session['email']
        )
        solution.date = datetime.now()
        solution.save()
        return HttpResponseRedirect(self.success_url)


class SolutionUpdateView(generic.UpdateView):
    model = Solution
    template_name = 'solutions/edit_solution.html'
    form_class = SolutionForm

    def get_success_url(self):
        return '/website/profile'
