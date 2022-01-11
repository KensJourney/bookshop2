from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')

class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='user')
        self.data1 = Product.objects.create(category_id=1, title='confetto', created_by_id=1,
                                            slug='confetto', price='20', image='download')
        #cself.data2 = Product.products.create(category_id=2, title='J. D. Sallinger - The catcher in the rye', created_by_id='user',
                                             #slug='j-d-sallinger-the-catcher-in-the-rye', price='25', image='51EqnTkohBL._SX307_BO1204203200_')


    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'confetto')