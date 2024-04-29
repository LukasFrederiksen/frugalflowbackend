from django.test import TestCase
from rest_framework import status
from project.apps.manufacture.models import Manufacture


class ManufactureTestCase(TestCase):

    def get_test_user_data(self):
        return {
            "cvr": 98763432,
            "name": "Peter",
            "contactperson": "Ole Jensen",
            "phone": "54324354",
            "email": "mail@mail.com",
            "website": "www.manufacturers.com",
            "picture_logo": "https://frugal.dk/wp-content/uploads/2022/02/fugal-white-logo.png",
            "isdeleted": False
        }

    # Test Create metode
    def test_create_manufacture(self):

        test_user = self.get_test_user_data()

        # Poster en ny manufacture via vores endpoint
        response = self.client.post('/api/manufactures/', test_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        manufacture = Manufacture.objects.filter(cvr="98763432").first()

        # Her går vi ud fra at manufacture object eksisterer
        self.assertIsNotNone(manufacture)

    def test_get_manufacture_by_id(self):
        test_user = self.get_test_user_data()

        # Laver en instans af manufacture i databasen
        manufacture = Manufacture.objects.create(**test_user)

        # Henter id`et på den manufacture der lige er lavet
        manufacture_id = manufacture.id

        # Laver et GET request til at hente id`et på manufacture. Follow true gør at vi følger url`en til at get på id.
        response = self.client.get(f'/api/manufactures/{manufacture_id}', follow=True)

        # Tjekker status koden
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Deserializer JSON formatet til et dictionary (response_data). Et dictionary er ligesom en variabel, men kan holde på key-value-pairs, altså mere kompleks data. Fx id = 1, name = "Kim"
        response_data = response.json()

        # Sammenligner om det data vi får tilbage passer med det vi forventer ud fra vores test user. Husk at kalde manufacture dictionary, så vi får alt dataen med over.
        print(response_data)
        self.assertEqual(response_data['manufacture']['cvr'], test_user['cvr'])
        self.assertEqual(response_data['manufacture']['name'], test_user['name'])

    def test_update_manufacture_by_id(self):
        test_user = self.get_test_user_data()

        # Laver en instans af manufacture i databasen
        manufacture = Manufacture.objects.create(**test_user)

        # Data der skal opdateres
        updated_data = {
            "name": "Kim"
        }

        # Henter id`et på den manufacture der lige er lavet, Simon
        manufacture_id = manufacture.id

        # Laver et PUT request til at hente id`et på manufacture. Follow true gør at vi følger url`en til at get på id.
        response = self.client.put(f'/api/manufactures/{manufacture_id}', updated_data, format='json', follow=True)

        response_data = response.json()

        # Tjekker status koden
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresher manufacture objectet og henter det nyeste data fra databasen
        manufacture.refresh_from_db()

        # Success test assertEqual da Peter er det samme navn som i vores manufacture instans.
        self.assertEqual(response_data["manufacture"]["name"], "Peter")

        # Sammenligner om det data vi får tilbage passer med det vi forventer ud fra vores updated_data. (NotEqual)
        self.assertNotEqual(manufacture.name, updated_data['name'])


    def test_get_all_manufactures(self):
        # Arrange
        test_users = [
            {"cvr": 98763432, "name": "Hans Peterson", "phone": "54324354", "email": "mail1@mail.com"},
            {"cvr": 87654321, "name": "Anna Johnson", "phone": "98765432", "email": "mail2@mail.com"},

        ]


        # Act
        # Her laver vi en instans af manufacture i test db, og getter den via get requestet.
        # Response.json deseralizer det vi får tilbage via response, så vi kan bruge det videre i testen.
        manufactures = [Manufacture.objects.create(**user) for user in test_users]
        response = self.client.get('/api/manufactures/')
        response_data = response.json()

        # Assert
        # Tjekker status koden, tjekker længden på test_users, tjekker længden + / - 1 fra test_users, derfor er de
        # "NotEqual"
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_data['results']), len(test_users))
        self.assertNotEqual(len(response_data['results']), len(test_users) - 1)
        self.assertNotEqual(len(response_data['results']), len(test_users) + 1)





