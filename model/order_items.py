from main import database


class Order_items(database.Model):
    order_item_id = database.Column(
        database.Integer, primary_key=True, autoincrement=True
    )
    order_id = database.Column(
        database.Integer, ForeignKey("order.order_id"), nullable=True
    )
    product_name = database.Column(database.string(255), nullable=False)
    quantity = database.Column(database.Integer, nullable=False)
    price = database.Column(database.Integer, nullable=False)
    description = database.Column(database.string(255), nullable=False)
    discount_amount = database.Column(database.Integer, nullable=False)
    created_at = database.Column(database.TIMESTAMP)
    updated_at = database.Column(database.TIMESTAMP)
