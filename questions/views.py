from django.views import generic
from django.urls import reverse_lazy
from .models import Question

class IndexView(generic.ListView):
    template_name = 'questions/index.html'
    context_object_name = 'question_list'

    def get_queryset(self):
      return Question.objects.all()

class CreateView(generic.edit.CreateView):
  template_name = 'questions/create.html'
  model = Question
  fields = ['message']
  success_url = reverse_lazy('questions:index')

class UpdateView(generic.edit.UpdateView):
    template_name = 'questions/update.html'
    model = Question
    fields = ['message']
    success_url = reverse_lazy('questions:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'questions/delete.html'
    model = Question
    success_url = reverse_lazy('questions:index')

