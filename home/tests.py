from rest_framework import status
from rest_framework.test import APITestCase
from .models import MenuItem, MenuType
import json


class MenuTests(APITestCase):
    PROTOCOL = 'http://'
    DOMAIN = 'www.navegabit.com'

    def setUp(self):
        element_type = MenuType()
        element_type.type = 'z',
        element_type.save()

        element = MenuItem()
        element.name = "Test"
        element.submenu = False
        element.url = self.PROTOCOL + self.DOMAIN
        element.icon = ''
        element.parent = None
        element.type = element_type
        element.save()

    def test_create_Menu(self):
        """
        Ensure we can create a new element object.
        """
        url = '/home/'

        data = {
            'name': 'ItemTestCase',
            'url': self.PROTOCOL + self.DOMAIN,
            'submenu': False,
            'icon': '',
            'parent': None,
            'type': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MenuItem.objects.count(), 2)

    def test_get_element(self):
        """
        Ensure we can get Menu.
        """
        url = '/home/?type=1'
        response = self.client.get(url)  # noqa
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json_obj = [
            {
                'id': 1,
                'name': 'Test',
                'url': self.PROTOCOL + self.DOMAIN,
                'submenu': False,
                'icon': '',
                'parent': None,
                'type': 1
            }
        ]
        self.assertEqual(json.loads(response.content), json_obj)

# Create your tests here.
