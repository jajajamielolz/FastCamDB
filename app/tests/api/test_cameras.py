"""Camera endpoint test suite."""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.models import Camera


@pytest.fixture(scope="function", autouse=True)
def populate_db(test_db: Session):
    """Populate db."""
    print("creating camera test objects and adding to db...")
    camera_1 = Camera(uuid="1", description="fake cam", name="Pentax P3")
    test_db.add(camera_1)

    test_db.commit()


def test_post_camera_ok(client: TestClient):
    """Test posting an camera."""
    response = client.post(
        "/cameras",
        json={"name": "Yashica T4", "description": "test"},
    )
    assert response.status_code == 200


def test_get_camera_ok(client: TestClient):
    """Test getting an camera."""
    response = client.get("/cameras/1")
    assert response.status_code == 200


def test_get_cameras_ok(client: TestClient):
    """Test getting all cameras."""
    response = client.get("/cameras")
    assert response.status_code == 200


def test_patch_cameras_ok(client: TestClient):
    """Test patching an camera."""
    response = client.patch("/cameras/1", json={"name": "3"})
    assert response.status_code == 200

