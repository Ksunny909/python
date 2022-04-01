from django.conf import settings
from decimal import Decimal
from shop.models import Doctor


class Cart(object):
    def __init__(self, request):
        """
        Инициализация корзины объектом request
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, doctor, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        doctor_id = str(doctor.id)
        if doctor_id not in self.cart:
            self.cart[doctor_id] = {'quantity': 0, 'price': str(doctor.price)}
        if update_quantity:
            self.cart[doctor_id]['quantity'] = quantity
        else:
            self.cart[doctor_id]['quantity'] += quantity
        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, doctor):
        """
        Remove a doctor from the cart
        :param doctor:
        :return:
        """
        doctor_id = str(doctor.id)
        if doctor_id in self.cart:
            del self.cart[doctor_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        doctor_ids = self.cart.keys()
        # get the product objects and add them to the cart
        doctors = Doctor.objects.filter(id__in=doctor_ids)
        for doctor in doctors:
            self.cart[str(doctor.id)]['doctor'] = doctor

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
#количество товаров в корзине
    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())
#очистка корзины покупок
    def clear(self):
        """
        remove cart from session
        :return:
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True