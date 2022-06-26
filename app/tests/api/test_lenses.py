"""Lens endpoint test suite."""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.models import Lens


@pytest.fixture(scope="function", autouse=True)
def populate_db(test_db: Session):
    """Populate db."""
    print("creating lens test objects and adding to db...")
    lens_1 = Lens(uuid="1", name="Distagon")
    test_db.add(lens_1)

    test_db.commit()


def test_post_simple_lens_ok(client: TestClient):
    """Test posting an lens."""
    # test creating basic entry
    response = client.post(
        "/lenses",
        json={"name": "Rokkor-x"},
    )
    assert response.status_code == 200

    # test creating an entry with the same name raises an error
    response = client.post(
        "/lenses",
        json={"name": "Rokkor-x"},
    )
    assert response.status_code == 409


def test_post_complex_lens_ok(client: TestClient):
    """Test posting an lens."""
    # test creating basic entry
    response = client.post(
        "/lenses",
        json=COMPLEX_CAMERA_JSON,
    )
    assert response.status_code == 200


def test_get_lens_ok(client: TestClient):
    """Test getting an lens."""
    response = client.get("/lenses/1")
    assert response.status_code == 200
    assert response.json().get('name') == 'Distagon'


def test_get_lenses_ok(client: TestClient):
    """Test getting all lenses."""
    response = client.get("/lenses")
    assert response.status_code == 200
    assert len(response.json()) == 1

    response = client.get("/lenses", params={"name": "Distagon"})
    assert response.status_code == 200
    assert len(response.json()) == 1

    response = client.get("/lenses", params={"name": "non-existing-lens"})
    assert response.status_code == 200
    assert len(response.json()) == 0


def test_patch_lenses_ok(client: TestClient):
    """Test patching an lens."""
    response = client.patch("/lenses/1", json={"name": "Updated Name"})
    assert response.status_code == 200
    response = client.get("/lenses/1")
    assert response.json().get('name') == 'Updated Name'


COMPLEX_CAMERA_JSON = {
  "name": "Contax 159 Quartz",
  "alternate_name": "Contax 159",
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