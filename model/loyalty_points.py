from main import database


class loyalty_points(database.Model):
    points_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    user_id = database.Column(
        database.String(255), database.Foreignkey("user.user_id"), nullable=False
    )
    points_balance = database.Column(database.String(255))
    created_at = database.Column(database.TIMESTAMP)
    reason = database.Column(database.String(255))
    status = database.Column(database, database.Enum("GAIN", "LOSS"))
