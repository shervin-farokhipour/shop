from datetime import datetime

class OrderItem:
    def __init__(self, item_id, product_obj, quantity, unit_price):
        self.id = item_id
        self.product = product_obj
        self.quantity = quantity
        self.unit_price = unit_price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("خطا: تعداد کالا در سفارش باید بیشتر از صفر باشد.")
        self._quantity = value


class Payment:
    def __init__(self, payment_id, amount, status, gateway):
        self.id = payment_id
        self.amount = amount
        self.status = status
        self.gateway = gateway


class Order:
    def __init__(self, order_id, buyer_obj, status="Pending"):
        self.id = order_id
        self.buyer = buyer_obj
        self.created_at = datetime.now()
        self.status = status
        self.total_price = 0.0

        # لیست  پرداخت (Composition)
        self.items = []
        self.payment = None

    def add_item(self, order_item_obj):
        """متدی برای اضافه کردن کالا به سبد/سفارش و آپدیت قیمت کل"""
        self.items.append(order_item_obj)
        self.total_price += (order_item_obj.unit_price * order_item_obj.quantity)

    def set_payment(self, payment_obj):
        """متدی برای ثبت وضعیت پرداخت سفارش"""
        self.payment = payment_obj