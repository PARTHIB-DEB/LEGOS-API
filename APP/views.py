from rest_framework.decorators import api_view
from rest_framework.response import Response
from APP.seriallizers import legoserializer, loginserializer
from APP.models import legos
from rest_framework.views import APIView
from rest_framework import viewsets

# Doing CRUD ops inside same tab (just changing the url not the tab!!)

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
        obj = legos.objects.get(comics=data['comics'])
        serializer = legoserializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request):
        data = request.data
        del_comic_name = data['comics']
        obj = legos.objects.get(comics=del_comic_name)
        obj.delete()
        return Response({"Message": f"{del_comic_name} lego-object is deleted"})
    
    

# Just for doing CRUD ops. in a new tab using ROUTER (After registering in ROUTER)

class legoViewSet(viewsets.ModelViewSet):
    serializer_class = legoserializer
    queryset = legos.objects.all()


@api_view(['GET', 'POST'])
def login(request):
    if request.method == "POST":
        data = request.data
        serializer = loginserializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data
            return Response(serializer.data)

        return Response(serializer.errors)
    else:
        return Response({"Message": "Other Methods are not allowed!!"})
