from main import database


class Cart_items(database.Model):

    cart_item_id = database.Model(database.Integer, PrimaryKey=True, Autoincrement=True)
    cart_id = database.Column(
        database.Integer, database.ForeignKey("user.user_id"), nullable=False
    )
    product_id = database.Column(
        database.Integer, database.ForeignKey("product.product_id"), nullable=False
    )
    quantity = database.Column(database.String(255), nullable=False)
    created_at = database.Column(database.TIMESTAMP)
    updated_at = database.Column(database.TIMESTAMP)
