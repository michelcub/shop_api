from rest_framework.serializers import ModelSerializer

from shop.product.models import Category, Product, Stock


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProductSerializer(ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"


class StockSerializer(ModelSerializer):
    product = ProductSerializer(many=False)

    class Meta:
        model = Stock
        fields = "__all__"
