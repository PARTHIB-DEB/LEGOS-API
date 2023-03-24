from rest_framework import serializers
from APP.models import legos

class legoserializer(serializers.ModelSerializer):
    class Meta:
        model=legos
        fields='__all__'