from django.test import TestCase
from .models import Editor,Pics,tags,Category,Location

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james = Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class PicsTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.shoot = Pics(title = 'Learn', post = 'lets learn today', editor = 'shoot', category = 'study', location = 'Juja', tags = '#tusome', pub_date = '2019-12-16', cover = 'cover.png')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.shoot,Pics))



