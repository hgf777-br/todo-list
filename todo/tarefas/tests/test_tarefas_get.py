from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertContains, assertHTMLEqual
import pytest


@pytest.fixture
def resposta(client: Client):
    return client.get(reverse('tarefas:home'))


def test_status_code(resposta):
    assert resposta.status_code == 200


def test_formulario_presente(resposta):
    assertContains(resposta, '<form')


def test_botao_submit(resposta):
    assertContains(resposta, '<button type="button"')
