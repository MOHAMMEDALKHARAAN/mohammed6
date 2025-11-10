from decimal import Decimal
from django.conf import settings
from .models import Product

class Cart:
    """
    🛒 إدارة سلة التسوق باستخدام الجلسة (Session)
    """
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        ➕ إضافة منتج إلى السلة أو تحديث كميته
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        """💾 حفظ التعديلات في الجلسة"""
        self.session.modified = True

    def remove(self, product):
        """❌ حذف منتج من السلة"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """🔁 تمرير المنتجات في السلة مع بياناتها"""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            item = self.cart[str(product.id)]
            item['product'] = product
            item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item

    def __len__(self):
        """📦 عدد العناصر في السلة"""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """💰 المجموع الكلي للسلة"""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """🧹 تفريغ السلة"""
        del self.session[settings.CART_SESSION_ID]
        self.save()
