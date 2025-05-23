from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API funcionando!"}

def test_create_item():
    response = client.post("/items/", json={"name": "Teste", "description": "Item de teste"})
    assert response.status_code == 200
    assert response.json() == {
        "message": "Item recebido",
        "item": {"name": "Teste", "description": "Item de teste"}
    }
