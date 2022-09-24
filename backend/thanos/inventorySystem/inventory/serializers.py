from rest_framework import serializers

# if there's more collection, then separate them using ','
# Example collection A and B, from Login.models import A, B
from inventory.models import Item

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
