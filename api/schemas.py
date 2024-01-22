from ninja import ModelSchema

from store.models import Discount, Product, Rating
from accounts.models import User


class ProductSchema(ModelSchema):
    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "price",
            "category",
            "price",
            "is_available",
            "tags",
        )


class ProductInSchema(ModelSchema):
    owner: User | None = None

    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "slug",
            "category",
            "price",
            "is_available",
            "tags",
        )


class DiscountInSchema(ModelSchema):
    user: User | None = None

    class Meta:
        model = Discount
        fields = (
            "product",
            "percentage",
            "name",
            "valid_till",
        )


class DiscountSchema(ModelSchema):
    class Meta:
        model = Discount
        fields = (
            "product",
            "percentage",
            "name",
            "valid_till",
        )


class RatingSchema(ModelSchema):
    class Meta:
        model = Rating
        fields = ("user", "product", "rating", "review")


class StatusSchema(ModelSchema):
    status: int
    message: str
