from rest_framework.serializers import ModelSerializer

from .models import Category, Product, Stock


class CategorySerializer(ModelSerializer):
    """
    Serializer for Category model.

    This serializer is used to serialize and deserialize Category instances.

    Attributes:
    - model: The model class to be serialized. In this case, it's the Category model.
    - fields: The fields to be included in the serialized representation. In this case, only the 'name' field is included.

    Methods:
    - None

    """

    class Meta:
        model = Category
        fields = ["name"]


class ProductSerializer(ModelSerializer):
    """
    Serializer for Product model.

    This serializer is used to serialize and deserialize Product instances.

    Parameters:
    - None

    Attributes:
    - categories (CategorySerializer): A nested serializer for the 'categories' field of the Product model. It is a list of Category instances, serialized using the CategorySerializer.

    Methods:
    - None

    Returns:
    - A ProductSerializer instance with the specified fields from the Product model.
    """

    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"


class StockSerializer(ModelSerializer):
    """
    Serializer for Stock model.

    This serializer is used to serialize and deserialize Stock instances.

    Parameters:
    - None

    Attributes:
    - product (ProductSerializer): A nested serializer for the 'product' field of the Stock model. It is a single Product instance, serialized using the ProductSerializer.

    Methods:
    - None

    Returns:
    - A StockSerializer instance with the specified fields from the Stock model.
    """

    product = ProductSerializer(many=False)

    class Meta:
        model = Stock
        fields = "__all__"
