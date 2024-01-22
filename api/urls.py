from typing import List
from ninja import NinjaAPI
from api.schemas import (
    DiscountInSchema,
    DiscountSchema,
    ProductInSchema,
    ProductSchema,
    RatingSchema,
    StatusSchema,
)

from store.models import Discount, Product, Rating
from .auth import SellerAuthentication

seller_auth = SellerAuthentication()
api = NinjaAPI(auth=seller_auth)


@api.post("/add-discount", response=StatusSchema)
async def addDiscount(request, payload: DiscountInSchema):
    try:
        Discount.objects.create(**payload.dict())
        return {"status": "201", "message": "Discount added successfully"}
    except Exception as e:
        return {"status": 400, "message": e}


@api.post("/add-product", response=StatusSchema)
async def addProduct(request, payload: ProductInSchema):
    try:
        Product.objects.create(**payload.dict())
        return {"status": "201", "message": "Product added successfully"}
    except Exception as e:
        return {"status": 400, "message": e}


@api.get("/products", response=List[ProductSchema])
async def getProducts(request):
    products = Product.objects.filter(owner=request.user)
    return products


@api.get("/discounts", response=List[DiscountSchema])
async def getDiscounts(request):
    discounts = Discount.objects.filter(product__owner=request.user)
    return discounts


@api.get("/rating", response=List[RatingSchema])
async def getRatings(request):
    ratings = Rating.objects.filter(product__owner=request.user)
    return ratings
