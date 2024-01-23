from django.test import SimpleTestCase

# Create your tests here.

class Tests(SimpleTestCase):
    def test_home(self):
        response=self.client.get('/')
        self.assertEquals(response.status_code,200)

    def test_about(self):
        response=self.client.get('/about/')
        self.assertEquals(response.status_code,200)
