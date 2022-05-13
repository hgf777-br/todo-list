from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from todo.tarefas.forms import TarefaForm, TarefaNovaForm
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
            tarefas_concluidas = list(Tarefa.objects.filter(feita=True).all())
            return render(request, 'tarefas/home.html',
                          context={'form': form, 'tarefas_pendentes': tarefas_pendentes,
                                   'tarefas_concluidas': tarefas_concluidas},
                          status=400)

    tarefas_pendentes = list(Tarefa.objects.filter(feita=False).all())
    tarefas_concluidas = list(Tarefa.objects.filter(feita=True).all())
    return render(request, 'tarefas/home.html',
                  context={'tarefas_pendentes': tarefas_pendentes,
                           'tarefas_concluidas': tarefas_concluidas}
                  )


def detalhe(request, tarefa_id):
    if request.method == 'POST':
        tarefa = Tarefa.objects.get(id=tarefa_id)
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            
    return redirect(reverse('tarefas:home'))

def apagar(request, tarefa_id):
    # if request.method == 'POST':
    Tarefa.objects.filter(id=tarefa_id).delete()
    return redirect(reverse('tarefas:home'))
