"""Lens endpoint test suite."""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.models import Lens
from app.tests.api.test_cameras import COMPLEX_CAMERA_JSON


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
        json=COMPLEX_LENS_JSON,
    )
    assert response.status_code == 200
    response = client.get("/lenses", params={"name": COMPLEX_LENS_JSON.get("name"), "min_shutter_speed": COMPLEX_LENS_JSON.get("min_focal_length")})
    assert response.json()[0].get('min_aperture') == COMPLEX_LENS_JSON.get('min_aperture')


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
    response = client.get("/lenses", params={"name": "Updated Name"})
    assert len(response.json()) == 1


def test_compatible_cameras(client: TestClient):
    """Test compatible cameras for lenses."""
    # create camera
    client.post(
        "/cameras",
        json=COMPLEX_CAMERA_JSON,
    )
    # create lens
    created_lens = client.post(
        "/lenses",
        json=COMPLEX_LENS_JSON,
    )
    assert created_lens.json().get('compatible_cameras')[0].get('name') == COMPLEX_CAMERA_JSON.get('name')


COMPLEX_LENS_JSON = {
  "manufacturer": {
    "name": "Yashica",
    "country": "Japan"
  },
  "lens_mount": {
    "name": "C/Y"
  },
  "name": "ML",
  "min_focal_length": 1,
  "max_focal_length": 25,
  "min_aperture": 2,
  "max_aperture": 16,
  "auto": True,
  "manual": True
}