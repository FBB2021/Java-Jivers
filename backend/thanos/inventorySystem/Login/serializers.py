from rest_framework import serializers

# if there's more collection, then separate them using ','
# Example collection A and B, from Login.models import A, B
from Login.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
