from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Job Tracker API is running"


def test_create_job():
    response = client.post(
        "/jobs",
        json={
            "filename": "sample.csv",
            "file_type": "csv"
        }
    )

    assert response.status_code == 201
    data = response.json()
    assert data["filename"] == "sample.csv"
    assert data["file_type"] == "csv"
    assert data["status"] == "queued"


def test_get_jobs():
    response = client.get("/jobs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_job_not_found():
    response = client.get("/jobs/999")
    assert response.status_code == 404