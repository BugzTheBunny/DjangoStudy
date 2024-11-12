from rest_framework import serializers
from reporting.models import Customer, Order, Product, Category, Supplier


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'customer',
            'product',
            'order_date',
            'shipped_name',
            'shipped_address',
            'shipped_postal_code',
            'shipped_country',
            'shipped_city',
            ]

    def to_representation(self, instance):
        self.fields['customer'] = CustomerSerializer(read_only=True)
        self.fields['product'] = ProductSerializer(read_only=True)
        return super(OrderSerializer,self).to_representation(instance)
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer              
        fields = [
            'id',
            'first_name',
            'last_name',
            'gender',
            'title',
            'address',
            'city',
            'region',
            'postal_code',
            'country',
            'phone',
            'email'
        ]

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = [
            'id',
            'product_name',
            'supplier',
            'category',
            'unit_price',
            'units_in_stock',
            'units_on_order',
        ]
    
    def to_representation(self, instance):
        self.fields['category'] = CategorySerializer(read_only=True)
        self.fields['supplier'] = SupplierSerializer(read_only=True)
        return super(ProductSerializer,self).to_representation(instance)

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]

class SupplierSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Supplier
        fields = [
            'company_name',
            'contact_name',
            'contact_title',
            'address',
            'city',
            'region',
            'postal_code',
            'country',
            'phone',
            'email',
            'webpage',
        ]