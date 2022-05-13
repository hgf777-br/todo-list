from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertContains, assertHTMLEqual
from todo.tarefas.models import Tarefa
import pytest


@pytest.fixture
def tarefa(db):
    return Tarefa.objects.create(nome='Tarefa', feita=False)


@pytest.fixture
def resposta(client, tarefa):
    resp = client.post(
        reverse('tarefas:apagar', kwargs={'tarefa_id': tarefa.id}))
    return resp


def test_tarefas_feita(resposta):
    assert not Tarefa.objects.exists()
