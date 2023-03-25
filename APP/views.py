from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from APP.seriallizers import legoserializer
from APP.models import legos
from rest_framework.views import APIView


class legolist(APIView):
    def get(self, request):
        serializer = legoserializer(legos.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = legoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def put(self, request):
        serializer = legoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def patch(self, request):
        data = request.data
        obj = legos.objects.get(id=data['id'])
        serializer = legoserializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request):
        data = request.data
        del_id = data['id']
        obj = legos.objects.get(id=del_id)
        obj.delete()
        return Response({"Message": f"Object of id {del_id} is deleted"})
