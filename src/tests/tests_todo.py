from pytest_django.asserts import assertContains


def test_index(client):
	response = client.get("/")
	assert response.status_code == 200
	assertContains(response, "Bienvenue!")
