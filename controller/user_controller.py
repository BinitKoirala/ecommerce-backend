from flask import request, jsonify
from ..model import Category
from ..database import database

from ..service.user_service import UserService


class UserController:

    user_service = UserService()

    def get_users(self):
        users = self.user_service.get_users()

        if not users:
            return {"message": "User not found."}, 404

        return [
            {
                "user_id": user.user_id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "dob": user.dob,
                "gender": user.gender,
                "address": user.address,
                "phone_number": user.phone_number,
                "role": user.role,
                "email": user.email,
                "status": user.status,
            }
            for user in users
        ], 200

    def get_user(self, id: int):
        user = self.user_service.get_user_by_id(id=id)

        if not user:
            return {"message": "User not found."}, 404

        return {
            "user_id": user.user_id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "dob": user.dob,
            "gender": user.gender,
            "address": user.address,
            "phone_number": user.phone_number,
            "role": user.role,
            "email": user.email,
            "status": user.status,
        }, 200

    def add_user(self):

        user_request: dict = request.get_json()

        response = self.user_service.create_user(user_detail=user_request)

        print(response)

        if not response:
            return {"message": "Unable to register user."}, 500

        return {
            "message": "User registration successful.",
            "data": jsonify(response),
        }, 201
