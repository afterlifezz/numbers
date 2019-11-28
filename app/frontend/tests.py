from django.test import TestCase


class SimpleTest(TestCase):
    def test_form(self):
        response = self.client.post('/', data={'number': '101101101'})
        self.assertEqual(response.context['text'], 'Sto jeden milionów sto jeden tysięcy sto jeden')
