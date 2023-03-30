from rest_framework import serializers
from APP.models import legos,register
from rest_framework.validators import UniqueTogetherValidator,UniqueValidator

class registerserializer(serializers.ModelSerializer):    
    class Meta:
        model = register
        fields = '__all__'
        validators = [
                UniqueValidator(
                    queryset=register.objects.all(),
                    message="Already Taken!!"
                )
            ]

class loginserializer(serializers.Serializer):
    Username=serializers.CharField()
    password=serializers.CharField()
    

class legoserializer(serializers.ModelSerializer):
    class Meta:
        model = legos
        fields = ['comics','names','total','seller']
        validators = [
                UniqueTogetherValidator(
                    queryset=legos.objects.all(),
                    fields=['comics','names'],
                    message="Don't Copy comic and character names!!"
                )
            ]
