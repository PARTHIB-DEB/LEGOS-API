from rest_framework import serializers
from APP.models import legos
from rest_framework.validators import UniqueTogetherValidator


class legoserializer(serializers.ModelSerializer):
    class Meta:
        model = legos
        fields = ['comics','names','seller']
        validators = [
                UniqueTogetherValidator(
                    queryset=legos.objects.all(),
                    fields=['comics','names'],
                    message="Don't Copy comic and character names!!"
                )
            ]
