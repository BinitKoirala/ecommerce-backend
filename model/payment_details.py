from main import database


class Payment_Details(database.Model):
    payment_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    order_id = database.Column(
        database.Integer, database.ForeignKey("order.order_id"), nullable=True
    )
    payment_date = database.Column(database.TIMESTAMP)
    payment_method = database.Column(
        database.String(255),
        Enum=("CREDIT CARD", "DEBIT CARD", "PAYPAL", "CASH ON DELIVERY"),
    )
    payment_status = database.Column(
        database.String(255), Enum=("PENDING", "COMPLETED", "FAILED", "REFUNDED")
    )
    created_at = database.Column(database.TIMESTAMP)
