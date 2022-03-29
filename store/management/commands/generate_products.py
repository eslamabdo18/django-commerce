from django.core.management.base import BaseCommand

from store.models import Product
from store.products import products as product_list


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        # print(product_list)
        for product in product_list:
            Product.objects.create(title=product['name'], image=product['image'], description=product['description'],
                                   price=product['price'], discounted_price=product['price'], category_id=4,author_id=1)
