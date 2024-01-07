"""Store Forms"""
from django.forms import ModelForm

from store.models import Category, Discount, Product


class ProductForm(ModelForm):
    """Product form to add/update new products"""

    class Meta:
        """Meta information"""

        model = Product
        fields = "__all__"


class DiscountForm(ModelForm):
    """Discount form"""

    class Meta:
        """Meta information"""

        model = Discount
        fields = "__all__"


class CategoryForm(ModelForm):
    """Form for creating/updating category"""

    class Meta:
        """Meta information"""

        model = Category
        fields = "__all__"
