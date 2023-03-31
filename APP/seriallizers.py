from rest_framework import serializers
from APP.models import *
from rest_framework.validators import UniqueTogetherValidator

class loginserializer(serializers.Serializer):
    Username=serializers.CharField()
    password=serializers.CharField()
    
class registerserializer(serializers.Serializer):    
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    class Meta:
        validators = [
                UniqueTogetherValidator(
                    queryset=register.objects.all(),
                    fields='__all__',
                    message="Already Taken!!"
                )
            ]
    

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
