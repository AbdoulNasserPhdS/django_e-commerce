from django.test import TestCase
from store.models import Product, SubCategory

# Create your tests here.

# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # les objects creer ici ne seront pas modifier aucours de tout les test
#         print("setUpTestData: Run once to set up non-modified data for all class methods.")
#         pass

#     def setUp(self):
#         # les objects creer ici seront modifier aucours des tests, chaque test recoivent un objet frai
#         print("setUp: Run once for every test method to setup clean data.")
#         pass

#     def test_false_is_false(self):
#         print("Method: test_false_is_false.")
#         self.assertFalse(False)

#     def test_false_is_true(self):
#         print("Method: test_false_is_true.")
#         self.assertTrue(False)

#     def test_one_plus_one_equals_two(self):
#         print("Method: test_one_plus_one_equals_two.")
#         self.assertEqual(1 + 1, 2)


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        sub=SubCategory.objects.create(name='menager')
        Product.objects.create(name="produit 3", stripe_product_id='stripe',category='VT',subCategory=sub)

    def test_first_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_first_name_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 128)

    # def test_object_name_is_last_name_comma_first_name(self):
    #     product = Product.objects.get(id=1)
    #     expected_object_name = f'{author.last_name}, {author.first_name}'
    #     self.assertEqual(str(author), expected_object_name)

    # def test_get_absolute_url(self):
    #     author = Author.objects.get(id=1)
    #     # This will also fail if the urlconf is not defined.
    #     self.assertEqual(author.get_absolute_url(), '/catalog/author/1')
