from django.test import TestCase
from django.urls import reverse

from store.models import Product, SubCategory





class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests*

        SubCategory.objects.create(name='Subcategory')

        number_of_product = 25

        for product_id in range(number_of_product):
            Product.objects.create(
                name=f'Product {product_id}',
                category='VT',
                subCategory=SubCategory.objects.get(id=1),
            )
    #  client permet de simuler un navigateur fictive
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    # def test_view_uses_correct_template(self):
    #     response = self.client.get(reverse('index'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'store/index.html')

    # def test_pagination_is_ten(self):
    #     response = self.client.get(reverse('index'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertTrue(len(response.context['product_list']) == 20)

    # def test_lists_all_authors(self):
    #     # Get second page and confirm it has (exactly) remaining 3 items
    #     response = self.client.get(reverse('authors')+'?page=2')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertTrue(len(response.context['author_list']) == 3)
