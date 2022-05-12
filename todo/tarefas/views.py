from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from todo.tarefas.forms import TarefaNovaForm
from todo.tarefas.models import Tarefa

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tarefas:home'))
        else:
            tarefas_pendentes = list(Tarefa.objects.filter(feita=False).all())
            return render(request, 'tarefas/home.html', context={'form': form, 'tarefas_pendentes': tarefas_pendentes}, status=400)
    
    tarefas_pendentes = list(Tarefa.objects.filter(feita=False).all())
    return render(request, 'tarefas/home.html', context={'tarefas_pendentes': tarefas_pendentes})