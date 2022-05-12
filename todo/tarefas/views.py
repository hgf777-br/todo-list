from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from todo.tarefas.forms import TarefaNovaForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tarefas:home'))
        else:
            return render(request, 'tarefas/home.html', context={'form': form}, status=400)
    return render(request, 'tarefas/home.html')