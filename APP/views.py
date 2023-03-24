from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from APP.seriallizers import legoserializer
from APP.models import legos
from rest_framework.views import APIView



# Create your views here.
# @api_view(['GET','POST'])
# def legosmethod(request):
#     if request.method == 'GET':
#         obj = legos.objects.all()
#         serializer=legoserializer(obj , many=True)
#         return Response(serializer.data)
    
#     else:
#         serializer=legoserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save
#             return Response(serializer.data)
        
#         return Response(serializer.errors)

class legolist(APIView):
    def get(self,request):
        obj = legos.objects.all()
        serializer=legoserializer(obj , many=True)
        print("****************")
        print(serializer.data)
        print("****************")
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer=legoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data)
        
        return Response(serializer.errors)