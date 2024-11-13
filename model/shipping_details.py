from main import database

class Shipping_details(database.Model):
    shipping_id = database.Column(database.Integer,primary_key=True, autoincrement=True)
    order_id = database.Column(database.Integer,ForeignKey("order.order_id"),nullable=False)
    tracking_number = database.Column(database.String(255))
    shipping_date = database.Column(database.TIMESTAMP)
    estimated_delivery_date = database.Column(database.TIMESTAMP)
    status = database.Column(database.Enum(('Pending', 'Shipped', 'In Transit', 'Delivered'))