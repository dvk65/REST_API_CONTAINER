import unittest, json
import rest_api as app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.create_app.config['TESTING'] = True
        self.app = app.create_app.test_client()

    def test_get_books_endpoint(self):
        b = self.app.get('/books')
        res = json.loads(b.data.decode('utf-8'))
        self.assertEqual(res[0]['title'], 'Green Beans') #b.data[0]['title']
        self.assertEqual(res[1]['title'], 'Slurp')

    def test_post_no_books_endpoint(self):
        b = self.app.post('/')
        self.assertEqual(b.status_code, 404)

    def test_get_book_endpoint(self):
        r = self.app.get('/books/1')
        self.assertEqual(r.json, {'author': 'Farmer', 'id': 1, 'title': 'Green Beans'})

    def test_post_book_endpoint(self):
        b = self.app.post('/books',
                          content_type='application/json',
                          data=json.dumps({'id': 3, 'title': 'Curls', 'author': 'Cam'}))
        self.assertEqual(b.json, {'location': f'/books/3'})
        self.assertEqual(b.status_code, 200)
    
    def test_put_book_endpoint(self):
        b = self.app.put('/books/4',
                          content_type='application/json',
                          data=json.dumps({'id': 4, 'title': 'Cheese', 'author': 'Remy'}))
        self.assertEqual(b.json, {'id': 4, 'title': 'Cheese', 'author': 'Remy'})
        self.assertEqual(b.status_code, 200)

    def test_delete_book_endpoint(self):
        b = self.app.delete('/books/3',
                          content_type='application/json',
                          data=json.dumps({'id': 3, 'title': 'Curls', 'author': 'Cam'}))
        self.assertEqual(b.json, {'id': 3, 'title': 'Curls', 'author': 'Cam'})
        self.assertEqual(b.status_code, 200)
    


if __name__ == '__main__':
    unittest.main()