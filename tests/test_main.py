import pytest

def test_create_leader(client):
    response = client.post(
        "/leaders/",
        json={"name": "Captain James Cutter", "faction": "UNSC", "background": "Experienced leader"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Captain James Cutter"
    assert response.json()["faction"] == "UNSC"

def test_read_leader(client):
    response = client.post(
        "/leaders/",
        json={"name": "Captain James Cutter", "faction": "UNSC", "background": "Experienced leader"}
    )
    assert response.status_code == 200

    response = client.get("/leaders/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Captain James Cutter"