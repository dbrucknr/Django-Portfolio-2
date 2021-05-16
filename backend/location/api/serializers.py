from rest_framework import serializers
from location.models import Zipcode

class ZipcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zipcode
        fields = '__all__'