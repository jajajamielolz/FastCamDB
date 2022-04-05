"""Auth overrides test suite."""


def test_auth_override(client):
    """Test auth overrides."""
    response = client.get("/me")
    print(response.json())
