from rest_framework import serializers
from .models import Employee, Item, Supply, Storage


class EmployeeSerizlizer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('name', 'surname')


class StorageSerizlizer(serializers.ModelSerializer):
    employee = EmployeeSerizlizer()

    class Meta:
        model = Storage
        fields = ('name', 'employee')

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('inventory_number', 'manufacturer', 'country', 'model')


class SupplySerializer(serializers.Serializer):
    item = ItemSerializer()
    storage = StorageSerizlizer()
    amount = serializers.IntegerField()
