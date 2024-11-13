from main import database


class Orders(database.Model):
    order_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    user_id = database.Column(
        database.Integer, ForeignKey("user.user_id"), nullable=True
    )
    status = database.Column(database.string(255), Enum=("Delivered", "Cancelled"))
    total_amount = database.Column(database.Integer, nullable=False)
    shipping_address = database.Column(database.string(255), nullable=False)
    billing_address = database.Column(database.string(255), nullable=False)
