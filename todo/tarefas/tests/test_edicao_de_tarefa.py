from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertContains, assertHTMLEqual
from todo.tarefas.models import Tarefa
import pytest


@pytest.fixture
def tarefa_pendente(db):
    return Tarefa.objects.create(nome='Tarefa', feita=False)


@pytest.fixture
def resposta_com_tarefa_pendente(client, tarefa_pendente):
    resp = client.post(reverse('tarefas:detalhe', kwargs={'tarefa_id': tarefa_pendente.id}),
                       data={'feita': 'true',
                             'nome': f'{tarefa_pendente.nome}-editada'}
                       )
    return resp


def test_tarefas_status_code(resposta_com_tarefa_pendente):
    assert resposta_com_tarefa_pendente.status_code == 302


def test_tarefas_feita(resposta_com_tarefa_pendente):
    assert Tarefa.objects.first().feita
