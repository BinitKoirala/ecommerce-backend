import os

from flask import Flask
from sqlalchemy.sql import text
from dotenv import load_dotenv


from .model import *
from .database import database, migrate
from .route.product_route import product_bp
from .route.user_route import user_bp
from .route.category_route import category_bp

load_dotenv()

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")


# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:admin1@127.0.0.1:5432/ecommerce"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

database.init_app(app)
migrate.init_app(app, database)


app.register_blueprint(product_bp)
app.register_blueprint(user_bp)
app.register_blueprint(category_bp)


@app.route("/")
def hello_world():
    # return "<p style ='color:red'>Hello, World!</p>"
    return {"message": "Welcome to Ecommerce API!"}


@app.route("/categories/<int:id>", methods=["GET"])
def get_category(id: int):
    category: Category = Category.query.get(id)

    return {
        "id": category.id,
        "name": category.name,
        "description": category.description,
    }


@app.route("/categories", methods=["GET"])
def list_category():

    categories = Category.query.all()

    return [
        {
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "created_at": category.created_at,
            "updated_at": category.updated_at,
        }
        for category in categories
    ]
