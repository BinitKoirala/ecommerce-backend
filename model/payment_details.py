from main import database


class Payment_Details(database.Model):
    payment_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    order_id = database.Column(
        database.Integer, ForeignKey("order.order_id"), nullable=True
    )
    payment_date = database.Column(database.TIMESTAMP)
    payment_method = database.Column(
        database.String(255),
        Enum=("Credit Card", "Debit Card", "PayPal", "Cash on Delivery"),
    )
    payment_status = database.Column(
        database.String(255), Enum=("Pending", "Completed", "Failed", "Refunded")
    )
    created_at = database.Column(database.TIMESTAMP)
