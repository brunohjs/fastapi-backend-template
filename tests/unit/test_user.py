import pytest
from fastapi.testclient import TestClient
from main import app  # Supondo que seu arquivo principal seja main.py

# Criar uma instância do cliente de teste
client = TestClient(app)


@pytest.fixture
def new_user():
    """Função que fornece dados de usuário para testar a criação"""
    return {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "password": "securepassword123"
    }


def test_create_user(new_user):
    """Teste para a criação de um novo usuário"""

    # Envia uma solicitação POST para a rota de criação de usuário
    response = client.post("/users/", json=new_user)

    # Verifica se o código de status é 201 (Created)
    assert response.status_code == 201

    # Verifica se a resposta contém os dados esperados
    response_data = response.json()
    assert response_data["username"] == new_user["username"]
    assert response_data["email"] == new_user["email"]
    assert "id" in response_data  # Verifica se o id do usuário foi retornado
