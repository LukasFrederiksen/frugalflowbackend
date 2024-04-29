from django.test import TestCase
from rest_framework import status
from project.apps.vessel.models import Vessel


class VesselTestCase(TestCase):
    def setUp(self):
        self.test_vessel_1 = {
            "name": "vessel_1",
            "imo": 1000,
            "type": "Container Ship",
            "isDeleted": False
        }
        self.test_vessel_2 = {
            "name": "vessel_2",
            "imo": 2000,
            "type": "Container Ship",
            "isDeleted": False
        }
        self.test_vessel_3 = {
            "name": "vessel_3",
            "imo": 3000,
            "type": "Container Ship",
            "isDeleted": False
        }
        self.test_vessel_to_update = {
            "name": "vessel_4",
            "imo": 4000,
            "type": "Container Ship",
            "isDeleted": False
        }

    def test_create_new_vessel(self):
        # --- Arrange
        # In setUp

        # --- Act
        response = self.client.post('/api/vessels/', self.test_vessel_1, format='json')
        response_data = response.json()

        # --- Assert
        # Testing if status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Testing if the name of the created vessel is as expected
        self.assertEqual(response_data["vessel"]["imo"], self.test_vessel_1["imo"])

    def test_get_vessel_by_id(self):
        # --- Arrange
        # In setUp

        # --- Act
        vessel = Vessel(**self.test_vessel_2)
        vessel.save()
        vessel_id = vessel.id
        response = self.client.get(f'/api/vessels/{vessel_id}')
        response_data = response.json()

        # --- Assert
        # Testing if status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Testing if the imo of the found vessel is as expected
        # Should pass
        self.assertEqual(response_data["vessel"]["imo"], self.test_vessel_2["imo"])  # imo = 2000
        # Should successfully fail
        self.assertNotEqual(response_data["vessel"]["imo"], 2001)   # imo = 2001

    def test_update_vessel_by_id(self):
        # --- Arrange
        # In setUp

        # --- Act
        vessel = Vessel(**self.test_vessel_3)
        vessel.save()
        vessel_id = vessel.id
        response = self.client.put(f'/api/vessels/{vessel_id}', self.test_vessel_to_update,
                                   content_type='application/json')
        response_data = response.json()

        # --- Assert
        # Testing if id of 1st version of vessel is correct
        self.assertEqual(vessel.imo, self.test_vessel_3["imo"])
        # Testing if status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Testing if the data from the updated vessel is as expected
        # Should pass
        self.assertEqual(response_data["vessel"]["name"], "vessel_4")
        self.assertEqual(response_data["vessel"]["imo"], 4000)
        # Should successfully fail
        self.assertNotEqual(response_data["vessel"]["name"], "vessel_5")
        self.assertNotEqual(response_data["vessel"]["imo"], 5000)

    def test_get_all_vessels(self):
        # --- Arrange
        # In setUp

        # --- Act
        # Adding 3 x vessels to list vessels
        vessels = [Vessel(**self.test_vessel_1), Vessel(**self.test_vessel_2), Vessel(**self.test_vessel_3)]
        for vessel in vessels:
            vessel.save()

        response = self.client.get(f'/api/vessels/')
        response_data = response.json()

        # --- Assert
        # Testing if the status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Testing if length of list of vessels is 3
        # ['results'] is needed because of the way pagination is used
        self.assertEqual(len(response_data['results']), 3)
        # Testing if length of list of vessels is !3
        self.assertNotEqual(len(response_data['results']), 2)
        self.assertNotEqual(len(response_data['results']), 4)
