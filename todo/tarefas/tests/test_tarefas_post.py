from django.test import Client
from django.urls import reverse
from todo.tarefas.models import Tarefa
import pytest


@pytest.fixture
def resposta(client: Client, db):
    return client.post(reverse('tarefas:home'), data={'nome': "Tarefa"})


def test_tarefa_existe_no_bd(resposta):
    assert Tarefa.objects.exists()


def test_redirct_after_save(resposta):
    assert resposta.status_code == 302


@pytest.fixture
def resposta_dado_invalido(client: Client, db):
    return client.post(reverse('tarefas:home'), data={'nome': ""})


def test_tarefa_nao_existe_no_bd(resposta_dado_invalido):
    assert not Tarefa.objects.exists()


def test_pagina_dados_invalidos(resposta_dado_invalido):
    assert resposta_dado_invalido.status_code == 400
