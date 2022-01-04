from django.conf.urls import url
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django .views.generic.edit import CreateView, UpdateView,DeleteView

from django . urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin


from . models import Task

class customLoginView(LoginView):
      template_name ='base/login.html'
      fields = '_all_'
      redirect_authenticated_User =True

      def get_success_url(self):
          return reverse_lazy('task')


class TaskList(LoginRequiredMixin ,ListView):
     model= Task
     context_object_name ="tasks"


     def get_context_data(self, **kwargs):
            return super().get_context_data(**kwargs)
            # context['color']= 'red'
            context['task']= context['tasks'].filter(User=self.request.user)
            context['count']= context['tasks'].filter(complete=False).count()
            return context

class TaskDetail(LoginRequiredMixin ,DetailView):
      model=Task
      context_object_name = 'task'
      template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin,CreateView):
      model = Task
      field = '_all_'
      success_url = reverse_lazy ('tasks')
    
      def form_valid(self,form):
          form.instance.user = self.request.user
          return super(TaskCreate,self).form_valid(form)

class Taskupdate(LoginRequiredMixin,UpdateView):
      model =Task
      fields = '_all_'
      success_url =reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin,DeleteView):
       model = Task
       context_object_name ='task'
       success_url =reverse_lazy('tasks')