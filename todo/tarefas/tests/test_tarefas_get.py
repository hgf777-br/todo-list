from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertContains, assertHTMLEqual
from todo.tarefas.models import Tarefa
import pytest


@pytest.fixture
def resposta(client: Client, db):
    return client.get(reverse('tarefas:home'))


def test_status_code(resposta):
    assert resposta.status_code == 200


def test_formulario_presente(resposta):
    assertContains(resposta, '<form')


def test_botao_submit(resposta):
    assertContains(resposta, '<button type="submit"')


@pytest.fixture
def lista_tarefas_pendentes(db):
    tarefas = [
        Tarefa(nome='Tarefa 1', feita=False),
        Tarefa(nome='Tarefa 2', feita=False)
    ]

    Tarefa.objects.bulk_create(tarefas)
    return tarefas


@pytest.fixture
def lista_tarefas_concluidas(db):
    tarefas = [
        Tarefa(nome='Tarefa 3', feita=True),
        Tarefa(nome='Tarefa 4', feita=True)
    ]

    Tarefa.objects.bulk_create(tarefas)
    return tarefas


@pytest.fixture
def resposta_com_lista_tarefas(client, lista_tarefas_pendentes, lista_tarefas_concluidas):
    return client.get(reverse('tarefas:home'))


def test_lista_tarefas_pendentes_presente(resposta_com_lista_tarefas, lista_tarefas_pendentes):
    for tarefa in lista_tarefas_pendentes:
        assertContains(resposta_com_lista_tarefas, tarefa.nome)


def test_lista_tarefas_concluidas_presente(resposta_com_lista_tarefas, lista_tarefas_concluidas):
    for tarefa in lista_tarefas_concluidas:
        assertContains(resposta_com_lista_tarefas, tarefa.nome)
