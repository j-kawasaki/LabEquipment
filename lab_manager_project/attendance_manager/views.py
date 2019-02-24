from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.views.generic import TemplateView
from attendance_manager.models import *

class StudentListView(TemplateView):
  template_name = 'student_list.html'

  def get(self, request, *args, **kwargs):
    context = super(StudentListView, self).get_context_data(**kwargs)
    teams = Team.objects.all()
    context['teams'] = teams

    return render(self.request, self.template_name, context)

