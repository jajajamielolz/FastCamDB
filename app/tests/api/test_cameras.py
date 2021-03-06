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
    response = client.get("/cameras", params={"name": COMPLEX_CAMERA_JSON.get("name"),
                                              "min_shutter_speed": COMPLEX_CAMERA_JSON.get("min_shutter_speed")})
    assert response.json()[0].get('lens_mount').get('name') == COMPLEX_CAMERA_JSON.get('lens_mount').get('name')


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
    response = client.get("/cameras", params={"name": "Updated Name"})
    assert len(response.json()) == 1


def test_partial_name_search(client: TestClient):
    """Test getting camera by partial name."""

    # confirm that partial search still returns camera
    response = client.get("/cameras", params={"name": "pen p"})
    assert response.status_code == 200
    assert len(response.json()) == 1

    # confirm that partial search doesn't include objects that shouldn't be returned
    response = client.get("/cameras", params={"name": "p4"})
    assert response.status_code == 200
    assert len(response.json()) == 0


# def test_min_max_shutter(client: TestClient):
#     """Test filtering on in max shutter speeds."""
#
#     # confirm that partial search still returns camera
#     response = client.get("/cameras", params={"min_shutter_speed": "0.125"})
#     assert response.status_code == 200
#     assert len(response.json()) == 1

# TODO: make compatible lens test


COMPLEX_CAMERA_JSON = {
    "name": "Contax 159 Quartz",
    "alternate_name": "Contax 159",
    "min_shutter_speed": 1,
    "max_shutter_speed": 1 / 1000,
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
