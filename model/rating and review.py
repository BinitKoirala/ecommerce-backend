from main import database


class Rating_and_Review(database.Model):
    review_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    order_id = database.Column(database.Integer, nullable=False)
    product_id = database.Column(
        database.String(255), ForeignKey("product.product_id"), nullable=False
    )
    user_id = database.Column(
        database.String(255), ForeignKey("user.user_id"), nullable=False
    )
    rating = database.Column(database.Integer, nullable=False)
    review_text = database.Column(database.String(255))
    created_at = database.Column(database.TIMESTAMP)
    uptaded_at = database.Column(database.TIMESTAMP)
