from rest_framework import serializers
from .models import Contact

# class ContactSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=100)
#     email=serializers.EmailField(max_length=254)
#     message=serializers.CharField()
#     mobile_number=serializers.CharField(max_length=10)

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['name', 'email', 'mobile_number',"message"]