from rest_framework.test import APIClient
from project.apps.manufacture.models import Manufacture


# Test data til brug i test
def create_test_manufacture_data():
    return {
        "cvr": "98763432",
        "name": "Hans Peterson",
        "contactperson": "Ole Jensen",
        "phone": "54324354",
        "email": "mail@mail.com",
        "website": "www.manufacturers.com",
        "picture_logo": "",
        "isdeleted": False
    }


# Laver en instans af vores Manufacture model, med test dataene ovenover
def create_manufacture_instance():
    manufacture_data = create_test_manufacture_data()
    return Manufacture.objects.create(**manufacture_data)


# APIClient bliver brugt til at sende http request til vores server (views). Det gør at vi kan lave http request i vores test miljø.
def create_test_client():
    return APIClient()
