"""This file contains the store models like product, category,etc. """
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from accounts.models import User


# Create your models here.
class Category(models.Model):
    """Category model for categorizing products"""

    cover = models.ImageField(upload_to="media/covers")
    name = models.CharField(max_length=30)
    description = models.TextField()
    slug = models.SlugField(blank=False, unique=True, max_length=30)
    objects = models.Manager()

    class Meta:
        """Extra information about the model"""

        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        """
        This method returns the URL of a particular object
        """
        return reverse("store:show-category", args=[self.slug])


class Product(models.Model):
    """Product model"""

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField()
    slug = models.SlugField(blank=False, unique=True, max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    listed_prices = models.PositiveIntegerField()
    display_price = models.PositiveIntegerField()
    date_added = models.DateField(auto_now=True)
    is_available = models.BooleanField(default=True)
    tags = TaggableManager()
    objects = models.Manager()

    class Meta:
        """Meta class for extra information"""

        ordering = ["-date_added"]

    def __str__(self) -> str:
        return str(self.name)

    def get_absolute_url(self):
        """
        This method returns the URL of a particular object
        """
        return reverse("store:show-product", args=[self.slug])


class Discount(models.Model):
    """Discount model for discounts"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    percentage = models.FloatField()
    name = models.CharField(max_length=20)
    valid_till = models.DateField()
    objects = models.Manager()


class ProductImage(models.Model):
    """Product image to store image information"""

    name = models.CharField(max_length=40)
    url = models.ImageField(upload_to="media/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantities = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    objects = models.Manager()


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    review = models.TextField()
    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "product"], name="unique rating")
        ]
