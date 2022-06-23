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


def test_post_simple_camera_ok(client: TestClient):
    """Test posting an camera."""
    # test creating basic entry
    response = client.post(
        "/cameras",
        json={"name": "Yashica T4", "description": "test creating a camera with just the name property"},
    )
    assert response.status_code == 200

    # test creating an entry with the same name raises an error
    response = client.post(
        "/cameras",
        json={"name": "Yashica T4", "description": "test creating a camera with just the name property"},
    )
    assert response.status_code == 409


def test_post_complex_camera_ok(client: TestClient):
    """Test posting an camera."""
    # test creating basic entry
    response = client.post(
        "/cameras",
        json=COMPLEX_CAMERA_JSON,
    )
    assert response.status_code == 200


def test_get_camera_ok(client: TestClient):
    """Test getting an camera."""
    response = client.get("/cameras/1")
    #    camera_1 = Camera(uuid="1", description="fake cam", name="Pentax P3")
    assert response.status_code == 200
    assert response.json().get('name') == 'Pentax P3'


def test_get_cameras_ok(client: TestClient):
    """Test getting all cameras."""
    response = client.get("/cameras")
    assert response.status_code == 200
    assert len(response.json()) == 1

    response = client.get("/cameras", params={"name": "Pentax P3"})
    assert response.status_code == 200
    assert len(response.json()) == 1

    response = client.get("/cameras", params={"name": "non-existing-camera"})
    assert response.status_code == 200
    assert len(response.json()) == 0

def test_patch_cameras_ok(client: TestClient):
    """Test patching an camera."""
    response = client.patch("/cameras/1", json={"name": "Updated Name"})
    assert response.status_code == 200
    response = client.get("/cameras/1")
    assert response.json().get('name') == 'Updated Name'


COMPLEX_CAMERA_JSON = {
  "name": "Contax 159 Quartz",
  "description": "Geat, simple camera.",
  "alternate_name": "Contax 159",
  "min_year": "2022-06-23T19:45:30.363Z",
  "max_year": "2022-06-23T19:45:30.363Z",
  "min_shutter_speed": 1/1000,
  "max_shutter_speed": 1,
  "auto_focus": False,
  "shutter_priority": False,
  "aperture_priority": True,
  "bulb_mode": True,
  "self_timer": True,
  "manual": True,
  "battery_required": True,
  "manufacturer": {
    "name": "Contax",
    "country": "Germany"
  },
  "lens_mount": {
    "name": "C/Y"
  },
  "metering": {
    "name": "TTL center-weighted",
  }
}