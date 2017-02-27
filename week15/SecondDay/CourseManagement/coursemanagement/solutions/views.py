from django.shortcuts import render
from django.views import generic
from datetime import datetime
from django.http import HttpResponseRedirect

from .forms import SolutionForm

from website.models import Student


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
