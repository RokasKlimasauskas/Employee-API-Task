import unittest
from app import create_app, db
from app.models import Employee

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Employee API!', response.data)

    def test_add_employee(self):
        response = self.client.post('/employee', json={
            'name': 'John Doe',
            'department': 'Engineering',
            'workflow': 0.8
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['name'], 'John Doe')

    def test_get_employees(self):
        self.client.post('/employee', json={
            'name': 'John Doe',
            'department': 'Engineering',
            'workflow': 0.8
        })
        response = self.client.get('/employees')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)

    def test_get_employee(self):
        self.client.post('/employee', json={
            'name': 'John Doe',
            'department': 'Engineering',
            'workflow': 0.8
        })
        response = self.client.get('/employee/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'John Doe')

    def test_update_employee(self):
        self.client.post('/employee', json={
            'name': 'John Doe',
            'department': 'Engineering',
            'workflow': 0.8
        })
        response = self.client.put('/employee/1', json={
            'name': 'Jane Doe',
            'department': 'HR',
            'workflow': 0.9
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'Jane Doe')

    def test_delete_employee(self):
        self.client.post('/employee', json={
            'name': 'John Doe',
            'department': 'Engineering',
            'workflow': 0.8
        })
        response = self.client.delete('/employee/1')
        self.assertEqual(response.status_code, 204)
        response = self.client.get('/employee/1')
        self.assertEqual(response.status_code, 404)

    def test_populate(self):
        response = self.client.post('/populate')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/employees')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 5)

if __name__ == '__main__':
    unittest.main()
