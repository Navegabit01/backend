from rest_framework import status
from rest_framework.test import APITestCase
from .models import Card, CardsType
import json


class CardsTests(APITestCase):
    PROTOCOL = 'http://'
    DOMAIN = 'www.navegabit.com'

    def setUp(self):
        card_type = CardsType()
        card_type.type = 'z',
        card_type.save()
        card = Card()
        card.title = 'Test'
        card.text = 'texto de prueba'
        card.active = False
        card.url = self.PROTOCOL + self.DOMAIN
        card.type = CardsType
        card.save()

    def test_create_cards(self):
        """
            Ensure we can create a new card object.
        """
        url = '/services/'

        data = {
            'tittle': 'Test',
            'text': 'texto de prueba',
            'active': False,
            'url': self.DOMAIN + self.PROTOCOL,
            'order': 0,
            'image': self.PROTOCOL + "127.0.0.1:8000/photos/modeloServicios.png",
            'type': 1
        }
        response = self.client.post(url, data, format='json')  # noqa
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Card.objects.count(), 2)

    def test_get_cards(self):
        """
                Ensure we can create a new card object.
            """
        url = '/services/?type=2'
        response = self.client.get(url)  # noqa
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json_obj = [
            {
                'id': 1,
                'tittle': 'Test',
                'text': 'texto de prueba',
                'active': False,
                'url': self.PROTOCOL + self.DOMAIN,
                'order': 0,
                'image': self.PROTOCOL + "127.0.0.1:8000/photos/modeloServicios.png",
                'type': 1
            }
        ]
        self.assertEqual(json.loads(response.content), json_obj)

# Create your tests here.
