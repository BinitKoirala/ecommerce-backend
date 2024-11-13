from ..service.category_service import CategoryService


class CategoryController:

    category_service = CategoryService()

    def get_categories(self):
        categories = self.category_service.get_categories()

        if not categories:
            return {"message": "Categories not found."}, 404

        return [
            {
                "id": category.id,
                "name": category.name,
                "description": category.description,
                "created_at": category.created_at,
                "updated_at": category.updated_at,
            }
            for category in categories
        ], 200

    def get_category(self, id: int):
        category = self.category_service.get_category_by_id(id=id)

        if not category:
            return {"message": "Category not found."}, 404

        return {
            "id": category.id,
            "name": category.name,
            "description": category.description,
        }, 200
